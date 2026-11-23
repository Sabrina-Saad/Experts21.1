#!/usr/bin/env python3
"""Validate the expert team: .claude/agents, .claude/skills, docs/expert-roster.md and CLAUDE.md.

Run from the project root:  python3 scripts/validate_team.py
Exits 1 and prints every problem if anything is inconsistent.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(ROOT, ".claude", "agents")
SKILLS_DIR = os.path.join(ROOT, ".claude", "skills")
ROSTER = os.path.join(ROOT, "docs", "expert-roster.md")
CLAUDE_MD = os.path.join(ROOT, "CLAUDE.md")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MIN_AGENTS, MAX_AGENTS = 10, 50

errors, warnings = [], []


def frontmatter(path):
    """Parse the simple YAML frontmatter used in this project (scalars and '- item' lists)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        errors.append(f"{rel(path)}: frontmatter must start with '---' on line 1")
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{rel(path)}: frontmatter is not closed with '---'")
        return {}, text
    try:
        import yaml  # optional, more exact
        data = yaml.safe_load(text[4:end]) or {}
    except ImportError:
        data, key = {}, None
        for line in text[4:end].splitlines():
            if re.match(r"^\s+-\s+", line) and key:
                data.setdefault(key, []).append(line.split("-", 1)[1].strip())
            elif ":" in line and not line.startswith(" "):
                key, val = line.split(":", 1)
                key, val = key.strip(), val.strip()
                data[key] = val.strip('"') if val else []
    except Exception as e:  # yaml error
        errors.append(f"{rel(path)}: YAML error: {e}")
        return {}, text
    return data, text[end + 5:]


def rel(p):
    return os.path.relpath(p, ROOT)


# ---- skills ----
skills = {}
if not os.path.isdir(SKILLS_DIR):
    errors.append(".claude/skills/ is missing")
else:
    for d in sorted(os.listdir(SKILLS_DIR)):
        p = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isfile(p):
            errors.append(f".claude/skills/{d}/ has no SKILL.md")
            continue
        fm, body = frontmatter(p)
        name = fm.get("name")
        if name != d:
            errors.append(f"{rel(p)}: name '{name}' must equal the directory name '{d}'")
        if not NAME_RE.match(d):
            errors.append(f"{rel(p)}: skill name must be lowercase-hyphen")
        desc = str(fm.get("description", "")) + str(fm.get("when_to_use", ""))
        if not fm.get("description"):
            errors.append(f"{rel(p)}: missing description")
        if len(desc) > 1536:
            errors.append(f"{rel(p)}: description + when_to_use is {len(desc)} chars (max 1536)")
        if fm.get("disable-model-invocation") in (True, "true"):
            warnings.append(f"{rel(p)}: disable-model-invocation is true, so agents cannot preload it")
        if body.count("\n") > 500:
            warnings.append(f"{rel(p)}: body is over 500 lines; move reference material to supporting files")
        skills[d] = fm

# ---- agents ----
agents = {}
if not os.path.isdir(AGENTS_DIR):
    errors.append(".claude/agents/ is missing")
else:
    for fn in sorted(os.listdir(AGENTS_DIR)):
        if not fn.endswith(".md"):
            continue
        p = os.path.join(AGENTS_DIR, fn)
        fm, body = frontmatter(p)
        name = fm.get("name")
        if not name:
            errors.append(f"{rel(p)}: missing name")
            continue
        if name != fn[:-3]:
            errors.append(f"{rel(p)}: name '{name}' should match the file name")
        if not NAME_RE.match(name) or ":" in name:
            errors.append(f"{rel(p)}: name must be lowercase-hyphen with no ':'")
        if name in agents:
            errors.append(f"{rel(p)}: duplicate agent name '{name}'")
        if not fm.get("description"):
            errors.append(f"{rel(p)}: missing description")
        sk = fm.get("skills") or []
        if isinstance(sk, str):
            sk = [s.strip() for s in sk.split(",") if s.strip()]
        for s in sk:
            if s not in skills:
                errors.append(f"{rel(p)}: skill '{s}' does not exist in .claude/skills/")
        if len(sk) != len(set(sk)):
            errors.append(f"{rel(p)}: duplicate skills")
        if len(sk) > 32:
            errors.append(f"{rel(p)}: more than 32 skills (only the first 32 preload)")
        if not body.strip():
            errors.append(f"{rel(p)}: empty system prompt")
        agents[name] = {"skills": sk, "fm": fm}

n = len(agents)
if not MIN_AGENTS <= n <= MAX_AGENTS:
    errors.append(f"team has {n} agents; keep it between {MIN_AGENTS} and {MAX_AGENTS}")
for req in ("orchestrator", "team-builder"):
    if req not in agents:
        errors.append(f"required agent '{req}' is missing")
used = {s for a in agents.values() for s in a["skills"]}
for s in skills:
    if s not in used:
        warnings.append(f"skill '{s}' is not used by any agent")

# ---- roster consistency ----
if not os.path.isfile(ROSTER):
    errors.append("docs/expert-roster.md is missing")
else:
    text = open(ROSTER, encoding="utf-8").read()
    part1 = text.split("## Part 1", 1)[-1].split("## Part 2", 1)[0]
    part2 = text.split("## Part 2", 1)[-1].split("## Part 3", 1)[0]
    roster_agents = {}
    for line in part1.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and cells[1].startswith("`"):
            roster_agents[cells[1].strip("`")] = re.findall(r"`([^`]+)`", cells[5])
    roster_skills = {}
    for line in part2.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[1].startswith("`"):
            roster_skills[cells[1].strip("`")] = re.findall(r"`([^`]+)`", cells[4])
    for a in agents:
        if a not in roster_agents:
            errors.append(f"roster: agent '{a}' is missing from Part 1")
        elif sorted(roster_agents[a]) != sorted(agents[a]["skills"]):
            errors.append(f"roster: skills for '{a}' differ from .claude/agents/{a}.md")
    for a in roster_agents:
        if a not in agents:
            errors.append(f"roster: lists agent '{a}' but .claude/agents/{a}.md does not exist")
    for s in skills:
        if s not in roster_skills:
            errors.append(f"roster: skill '{s}' is missing from Part 2")
        else:
            actual = sorted(a for a in agents if s in agents[a]["skills"])
            if sorted(roster_skills[s]) != actual:
                errors.append(f"roster: 'Used by' for '{s}' should be {actual}")
    for s in roster_skills:
        if s not in skills:
            errors.append(f"roster: lists skill '{s}' but .claude/skills/{s}/SKILL.md does not exist")
    m = re.search(r"\*\*(\d+) agents · (\d+) skills", text)
    if not m or (int(m.group(1)), int(m.group(2))) != (n, len(skills)):
        errors.append(f"roster: header counts should read '**{n} agents · {len(skills)} skills'")

# ---- CLAUDE.md ----
if not os.path.isfile(CLAUDE_MD):
    errors.append("CLAUDE.md is missing")
else:
    t = open(CLAUDE_MD, encoding="utf-8").read()
    if f"{n} agents" not in t or f"{len(skills)} skills" not in t:
        errors.append(f"CLAUDE.md: update the counts to '{n} agents' and '{len(skills)} skills'")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"\n{n} agents, {len(skills)} skills — {'OK' if not errors else f'{len(errors)} error(s)'}")
sys.exit(1 if errors else 0)
