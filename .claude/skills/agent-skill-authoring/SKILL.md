---
name: agent-skill-authoring
description: "Creates, updates and validates project subagents and skills so the expert team stays consistent. Use when adding a new expert agent or skill, improving an existing one, or fixing the team's wiring."
---

# Agent & skill authoring

Creates, updates and validates project subagents and skills so the expert team stays consistent.

**Skill ID:** SK-46 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when adding a new expert agent or skill, improving an existing one, or fixing the team's wiring.

## Procedure

1. Check what exists: list `.claude/agents/` and `.claude/skills/`, and read `docs/expert-roster.md`. Reuse or extend an existing skill before creating a new one.
2. Agents: create `.claude/agents/<name>.md` with YAML frontmatter on line 1: `name` (lowercase-hyphen, matches the file name), `description` (what it does + 'Use for…' so delegation works), `tools`, `skills` (list of skill directory names), optional `color`. Body = the system prompt: role, responsibilities, docs to read, how to work, output format, handoffs, guardrails.
3. Skills: create `.claude/skills/<name>/SKILL.md` with frontmatter `name` (= directory name) and `description` (what + when, under 1,536 characters including `when_to_use`). Body: purpose, when to use, procedure, output, project context, guardrails. Keep under 500 lines; move long reference material to supporting files in the same folder.
4. Wire it: add the skill to the `skills:` list of every agent that should use it, and add new agents to the orchestrator's routing knowledge via the roster.
5. Update `docs/expert-roster.md` (agent table, skill table, 'Used by') and the counts in `CLAUDE.md`.
6. Run `python3 scripts/validate_team.py` and fix every error before finishing.
7. To improve an agent or skill: read it, collect the failure (what went wrong, example), make the smallest change that fixes it, and re-validate.

## Output

- List of files created/changed.
- Validator output (must pass).
- One-line summary of what changed and why.

## Project context

- Official docs: https://code.claude.com/docs/en/sub-agents and https://code.claude.com/docs/en/skills. Key facts: `skills:` in an agent preloads the full skill content; skills with `disable-model-invocation: true` can't be preloaded; agent `name` can't contain ':'; keep the team between 10 and 50 agents.

## Guardrails

- Everything lives inside this project (`.claude/`, `docs/`, `scripts/`); never write to `~/.claude/`.
- Don't grant an agent more tools than its job needs.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
