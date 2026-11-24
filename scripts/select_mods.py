#!/usr/bin/env python3
"""Rebuild the catalogue's candidate set from the scanned mod dataset.

Reads docs/MOD-DATA-full.csv and applies the catalogue's selection rules:
- one mod per repository (repo_mod_count == 1)
- repositories flagged as inflated or first-party are excluded
- the mod's core score is above MIN_CORE

core = stars / N, where N = max(1, ceil(days_since_update / 15)).
"""
import argparse
import csv
import json
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MIN_CORE = 100.0
EXCLUDED_REPOS = {
    "ruvnet/RuView",
    "ruvnet/ruflo",
    "Yeachan-Heo/oh-my-claudecode",
    "anthropics/claude-plugins-official",
    "avelikiy/great_cto",
}
NAME_OVERRIDES = {"claude-council": "council", "claude-carbon": "carbon"}

def core_of(row):
    stars = int(row.get("own_stars") or row.get("stars") or 0)
    days = int(row.get("days_since") or 0)
    return stars / max(1, math.ceil(days / 15))

def select(dataset):
    chosen = []
    for row in csv.DictReader(dataset.open(encoding="utf-8-sig")):
        if row.get("repo_mod_count") != "1":
            continue
        if row.get("repo") in EXCLUDED_REPOS:
            continue
        core = core_of(row)
        if core <= MIN_CORE:
            continue
        chosen.append((core, row))
    chosen.sort(key=lambda x: -x[0])
    return chosen

def listed_names():
    data = json.loads((ROOT / "community.json").read_text(encoding="utf-8"))
    return {m["name"] for m in data}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=str(ROOT / "docs" / "MOD-DATA-full.csv"))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    chosen = select(pathlib.Path(args.dataset))
    names = {NAME_OVERRIDES.get(row["mod"], row["mod"]) for _, row in chosen}
    print(f"{len(names)} mods score above {MIN_CORE:g}: (dataset {args.dataset})")
    for core, row in chosen:
        print(f"  {core:8.1f}  n={max(1, math.ceil(int(row.get('days_since') or 0) / 15))}  {row['mod']:<26} {row['repo']}")

    if not args.check:
        return 0

    listed = listed_names()
    added = sorted(names - listed)
    dropped = sorted(listed - names)
    if not added and not dropped:
        print("catalogue is up to date")
        return 0
    print("drift detected:")
    for n in added:
        print(f"  + {n} (qualifies, not listed)")
    for n in dropped:
        print(f"  - {n} (listed, no longer qualifies)")
    return 1

if __name__ == "__main__":
    sys.exit(main())
