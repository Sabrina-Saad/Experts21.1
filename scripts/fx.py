#!/usr/bin/env python3
"""Currency exchange rates from the Frankfurter API (https://api.frankfurter.dev, no API key).

Rates are European Central Bank reference rates, published once per working day (around 16:00 CET).
About 30 currencies are covered; run `currencies` to see them.

Usage (from the project root):
  python3 scripts/fx.py latest [BASE] [SYMBOLS]        e.g.  latest USD EUR,GBP,JPY
  python3 scripts/fx.py convert AMOUNT FROM TO [DATE]  e.g.  convert 1500 USD EUR
  python3 scripts/fx.py history FROM TO START [END]    e.g.  history USD JPY 2026-01-01 2026-11-20
  python3 scripts/fx.py currencies
Add --json to any command for the raw API response.
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.frankfurter.dev/v1"


def get(path, **params):
    q = {k: v for k, v in params.items() if v is not None}
    url = f"{API}/{path}" + (f"?{urllib.parse.urlencode(q)}" if q else "")
    req = urllib.request.Request(url, headers={"User-Agent": "experts21-fx/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        sys.exit(f"Frankfurter error {e.code} for {url}: {body}\n"
                 "If a currency is 'not found', it is not covered by ECB rates (run `currencies`).")
    except urllib.error.URLError as e:
        sys.exit(f"Could not reach {API}: {e.reason}. Is api.frankfurter.dev allowed by the network?")


def main(argv):
    raw = "--json" in argv
    args = [a for a in argv if a != "--json"]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = args[0], args[1:]
    if cmd == "currencies":
        data = get("currencies")
        if raw:
            print(json.dumps(data, indent=2))
        else:
            for code, name in sorted(data.items()):
                print(f"{code}  {name}")
    elif cmd == "latest":
        base = (rest[0] if rest else "USD").upper()
        symbols = rest[1].upper() if len(rest) > 1 else None
        data = get("latest", base=base, symbols=symbols)
        if raw:
            print(json.dumps(data, indent=2))
        else:
            print(f"1 {data['base']} on {data['date']} (ECB reference rate):")
            for code, rate in sorted(data["rates"].items()):
                print(f"  {code}  {rate}")
    elif cmd == "convert":
        if len(rest) < 3:
            sys.exit("usage: convert AMOUNT FROM TO [YYYY-MM-DD]")
        amount, frm, to = float(rest[0]), rest[1].upper(), rest[2].upper()
        path = rest[3] if len(rest) > 3 else "latest"
        data = get(path, base=frm, symbols=to, amount=amount)
        if raw:
            print(json.dumps(data, indent=2))
        else:
            print(f"{amount:,.2f} {frm} = {data['rates'][to]:,.2f} {to}  (ECB rate for {data['date']})")
    elif cmd == "history":
        if len(rest) < 3:
            sys.exit("usage: history FROM TO START [END]")
        frm, to, start = rest[0].upper(), rest[1].upper(), rest[2]
        end = rest[3] if len(rest) > 3 else ""
        data = get(f"{start}..{end}", base=frm, symbols=to)
        if raw:
            print(json.dumps(data, indent=2))
            return
        series = [(d, r[to]) for d, r in sorted(data["rates"].items())]
        vals = [v for _, v in series]
        print(f"{frm}->{to} from {data['start_date']} to {data.get('end_date', 'latest')}: {len(series)} data points")
        print(f"  first {vals[0]}  last {vals[-1]}  change {100 * (vals[-1] / vals[0] - 1):+.2f}%")
        print(f"  low {min(vals)}  high {max(vals)}")
    else:
        sys.exit(f"unknown command '{cmd}'. Run with --help.")


if __name__ == "__main__":
    main(sys.argv[1:])
