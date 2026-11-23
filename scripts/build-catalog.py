#!/usr/bin/env python3
"""Regenerates .claude-plugin/marketplace.json and every README from
community.json (the mods, each pinned to a checked commit),
readme/summaries.json (each mod's one-line summary per language),
readme/strings.json (table labels per language) and readme/pages/<lang>.md.

    python3 scripts/build-catalog.py
"""
import json
import pathlib
import os

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKET = ROOT / ".claude-plugin" / "marketplace.json"
# GitHub tables size columns to their content and strip widths, so the first
# column is widened with non-breaking spaces in its header.
FIRST_COLUMN_PAD = "&nbsp;" * 31
CATEGORY_ORDER = ["dashboards", "agents", "productivity", "rendering", "safety", "git", "fun"]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write(path, text):
    path.write_bytes(text.encode("utf-8"))


def source_of(mod):
    url = f"https://github.com/{mod['repo']}.git"
    if not mod["path"]:
        return {"source": "url", "url": url, "sha": mod["sha"]}
    return {"source": "git-subdir", "url": url, "path": mod["path"], "sha": mod["sha"]}


def homepage(mod):
    return f"https://github.com/{mod['repo']}/tree/{mod['sha']}/{mod['path']}".rstrip("/")


def check(mods, summaries, strings):
    names = [m["name"] for m in mods]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise SystemExit(f"duplicate plugin names: {sorted(dupes)}")
    for m in mods:
        if m["category"] not in CATEGORY_ORDER:
            raise SystemExit(f"{m['name']}: unknown category {m['category']}")
        # Missing translations fall back to the English description in catalog().


def build_market(mods):
    market = json.loads(MARKET.read_text(encoding="utf-8"))
    market["plugins"] = [{
        "name": m["name"], "source": source_of(m), "description": m["description"],
        "version": m["version"], "author": {"name": m["repo"].split("/")[0]},
        "homepage": homepage(m), "license": m["license"], "category": m["category"],
    } for m in mods]
    write(MARKET, json.dumps(market, indent=2, ensure_ascii=False) + "\n")


def language_bar(strings, current):
    return " · ".join(
        f"**{s['label']}**" if lang == current else f"[{s['label']}]({s['file']})"
        for lang, s in strings.items())


def catalog(mods, summaries, s, lang, images):
    lines = []
    for key in CATEGORY_ORDER:
        group = [m for m in mods if m["category"] == key]
        if not group:
            continue
        lines += [f"### {s['categories'][key]}", ""]
        for m in group:
            name = m["name"]
            link = homepage(m)
            text = summaries.get(name, {}).get(lang, m["description"])
            text = text.replace("|", "\\|")
            reach = ", ".join(s["reach"][a] for a in m["access"] if a in s["reach"]) or "—"
            author = m["repo"].split("/")[0]

            pics = images.get(m["repo"], [])
            if pics:
                url = pics[0]
                if url.startswith("/"):
                    url = "https://github.com" + url
                elif not url.startswith(("http://", "https://")):
                    url = url.replace(os.sep, "/")
                lines += [f"[![{name}]({url})]({link})", ""]

            lines += [f"#### [`{name}`]({link})", "",
                      f"*{s['by']} {author}* · {text}", "",
                      f"**{s['columns'][2]}:** {reach}", "",
                      f"`/plugin install {name}@best-claude-code-mods`", ""]
        lines.append("")
    return "\n".join(lines).rstrip()

def main():
    mods = load("community.json")
    summaries = load("readme/summaries.json")
    strings = load("readme/strings.json")
    images = load("readme/images.json")
    check(mods, summaries, strings)
    build_market(mods)
    for lang, s in strings.items():
        page = (ROOT / "readme" / "pages" / f"{lang}.md").read_text(encoding="utf-8")
        page = (page.replace("{{languages}}", language_bar(strings, lang))
                    .replace("{{count}}", str(len(mods)))
                    .replace("{{catalog}}", catalog(mods, summaries, s, lang, images)))
        write(ROOT / s["file"], page)
    print(f"{len(mods)} mods; {len(strings)} READMEs")


if __name__ == "__main__":
    main()
