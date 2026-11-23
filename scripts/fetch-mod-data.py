#!/usr/bin/env python3
"""Refresh docs/MOD-DATA-full.csv from the scanned upstream dataset.

Clones karanb192/awesome-claude-code-mods (shallow), reads its data/mods.json,
and writes one row per real mod with the columns the catalogue's rules read:
repo_mod_count, stars, own_stars, days_since, created, age_days, etc.

    python3 scripts/fetch-mod-data.py [--source owner/repo]
"""
import argparse
import csv
import datetime
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "MOD-DATA-full.csv"

KW = [
    ('Dashboard / usage / context', ['context bar','context window','context meter','usage','token','cache','burn','cost','spend','balance','quota','rate limit','context usage','context monitor','token budget']),
    ('Status line / band', ['status line','statusline','status bar','band above','line above','above the prompt','under the prompt','header','footer','ticker']),
    ('Subagent / agent orchestration', ['subagent','sub-agent','agent flow','agent radar','agent pane','teammate','spawn','fan-out','orchestrat','agent tree','agent crew','mission control']),
    ('Guard / safety / permissions', ['guard','hold','block','before it runs','risky','dangerous','permission','secret','redact','deny','blast radius','scope','safety']),
    ('Model routing / effort', ['reasoning effort','effort','router','routing','model picker','haiku','sonnet','opus']),
    ('Session / memory / handoff', ['session','handoff','compact','memory','resume','checkpoint','time machine','rewind','restore','history','snapshot']),
    ('Rendering / UI / theme', ['render','markdown','mermaid','theme','skin','syntax','highlight','chart','diagram','copy button','pretty','beautif','display']),
    ('Browser / web / network', ['browser','website','playwright','http','fetch','network']),
    ('Git / PR / CI / deploy', ['git','github','pull request','merge','commit','deploy','branch','diff','vercel']),
    ('Productivity / workflow', ['todo','task','plan','progress','next step','note','workflow','journal','command shelf','pin','memo','queue','decision','ledger','assumption','verify','doctor','inspector','dependency']),
    ('Fun / novelty', ['game','snake','tetris','pet','pokemon','music','spotify','now playing','reels','youtube','prayer','stock','breath','mindful','arcade','chess']),
]

def classify(m):
    txt = (m.get('description') or '').lower() + ' ' + (m.get('name') or '').lower()
    for cat, kws in KW:
        if any(k in txt for k in kws):
            return cat
    return 'Other / misc'

def days_since(ts, today):
    if not ts:
        return ''
    d = datetime.datetime.fromisoformat(ts.replace('Z', '+00:00')).date()
    return (today - d).days

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source', default='karanb192/awesome-claude-code-mods')
    args = ap.parse_args()

    today = datetime.date.today()
    tmp = tempfile.mkdtemp()
    try:
        subprocess.run(['git', 'clone', '--depth', '1', '--quiet',
                        f'https://github.com/{args.source}.git', tmp], check=True)
        data = json.loads((pathlib.Path(tmp) / 'data' / 'mods.json').read_text(encoding='utf-8'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    mods = [m for m in data['mods'] if m.get('kind') == 'mod']
    repo_count = {}
    for m in mods:
        repo_count[m['repo']] = repo_count.get(m['repo'], 0) + 1

    rows = []
    for m in mods:
        stars = m.get('stars') or 0
        n = repo_count[m['repo']]
        created = m.get('createdAt') or ''
        created_date = created[:10] if created else '?'
        age = days_since(created, today) if created else '?'
        reach = m.get('reach') or {}
        validate = m.get('validate')
        status = validate.get('status') if isinstance(validate, dict) else validate
        rows.append({
            'mod': m.get('name'), 'type': classify(m), 'repo': m.get('repo'),
            'path': m.get('path'), 'lines': 'n/a', 'stars': stars,
            'own_stars': stars if n == 1 else '', 'repo_mod_count': n,
            'project': 'karanb192', 'last_update': (m.get('pushedAt') or '')[:10],
            'days_since': days_since(m.get('pushedAt'), today),
            'created': created_date, 'age_days': age, 'screenshot': 'n/a',
            'reach': reach.get('name') if isinstance(reach, dict) else reach,
            'validate': status,
        })

    rows.sort(key=lambda r: (-int(r['stars'] or 0), r['mod'] or ''))
    fields = list(rows[0].keys())
    with OUT.open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f'wrote {OUT} ({len(rows)} mods, dataset {data.get("generated", "?")})')
    return 0

if __name__ == '__main__':
    sys.exit(main())
