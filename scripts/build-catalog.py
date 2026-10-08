#!/usr/bin/env python3
"""Regenerates .claude-plugin/marketplace.json and the README catalogue from
community.json (mods hosted elsewhere, each pinned to a commit) plus the mods
that live in this repository.

    python3 scripts/build-catalog.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKET = ROOT / ".claude-plugin" / "marketplace.json"
README = ROOT / "README.md"
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"

CATEGORIES = [
    ("ours", "From this repo", "本仓库自制"),
    ("dashboards", "Dashboards and usage", "仪表盘与用量"),
    ("agents", "Agents and subagents", "Agent 与子 agent"),
    ("productivity", "Productivity and context", "效率与上下文"),
    ("rendering", "Rendering and previews", "渲染与预览"),
    ("safety", "Safety and guards", "安全与守卫"),
    ("git", "Git, PRs and deploys", "Git、PR 与部署"),
    ("fun", "While you wait", "等待时的消遣"),
]
# What the validator reports a mod calls, for the access column.
ACCESS = {"http": "network", "process": "runs commands", "model": "model calls",
          "fs": "files", "mcp": "MCP"}

OURS = [
    {"name": "env-guard", "category": "ours", "license": "MIT",
     "description": "Refuses reads and edits of .env files.",
     "zh": "拒绝 Claude 读取或修改 .env 文件", "access": []},
    {"name": "turn-band", "category": "ours", "license": "MIT",
     "description": "A row above the prompt with the last turn's time and tool-call count.",
     "zh": "输入框上方显示上一轮用时和工具调用次数", "access": []},
]


def write(path, text):
    path.write_bytes(text.encode("utf-8"))


def source_of(mod):
    url = f"https://github.com/{mod['repo']}.git"
    if not mod["path"]:
        return {"source": "url", "url": url, "sha": mod["sha"]}
    return {"source": "git-subdir", "url": url, "path": mod["path"], "sha": mod["sha"]}


def homepage(mod):
    return f"https://github.com/{mod['repo']}/tree/{mod['sha']}/{mod['path']}".rstrip("/")


def main():
    community = json.loads((ROOT / "community.json").read_text(encoding="utf-8"))
    names = [m["name"] for m in OURS + community]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise SystemExit(f"duplicate plugin names: {sorted(dupes)}")

    market = json.loads(MARKET.read_text(encoding="utf-8"))
    plugins = [{"name": m["name"], "source": f"./{m['name']}", "description": m["description"],
                "category": "ours", "license": m["license"]} for m in OURS]
    for m in community:
        plugins.append({
            "name": m["name"], "source": source_of(m), "description": m["description"],
            "version": m["version"], "author": {"name": m["repo"].split("/")[0]},
            "homepage": homepage(m), "license": m["license"], "category": m["category"],
        })
    market["plugins"] = plugins
    write(MARKET, json.dumps(market, indent=2, ensure_ascii=False) + "\n")

    lines = []
    everything = [dict(m, ours=True) for m in OURS] + community
    for key, en, zh in CATEGORIES:
        mods = [m for m in everything if m["category"] == key]
        if not mods:
            continue
        lines += [f"### {en} · {zh}", "",
                  "| Mod | What it does | 说明 | Reaches |", "| --- | --- | --- | --- |"]
        for m in mods:
            link = f"[`{m['name']}`]({m['name']})" if m.get("ours") else f"[`{m['name']}`]({homepage(m)})"
            by = "" if m.get("ours") else f"<br><sub>by {m['repo'].split('/')[0]}</sub>"
            reach = ", ".join(ACCESS[a] for a in m["access"] if a in ACCESS) or "—"
            desc = m["description"].replace("|", "\|")
            lines.append(f"| {link}{by} | {desc} | {m['zh']} | {reach} |")
        lines.append("")
    table = "\n".join(lines).rstrip() + "\n"

    readme = README.read_text(encoding="utf-8")
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    write(README, f"{head}{START}\n{table}{END}{tail}")
    print(f"{len(plugins)} plugins in the marketplace")


if __name__ == "__main__":
    main()
