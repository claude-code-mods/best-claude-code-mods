#!/usr/bin/env bash
# Usage: scripts/new-mod.sh <mod-name> ["one-line description"]
# Copies template/ to <mod-name>/ and lists the new mod in the marketplace.
set -euo pipefail
cd "$(dirname "$0")/.."

name="${1:?usage: scripts/new-mod.sh <mod-name> [description]}"
description="${2:-TODO: say what $name does}"
[[ "$name" =~ ^[a-z][a-z0-9-]*$ ]] || { echo "mod name must be kebab-case: $name" >&2; exit 1; }
[[ -e "$name" ]] && { echo "$name already exists" >&2; exit 1; }

cp -R template "$name"
mv "$name/tests/mod-template.test.ts" "$name/tests/$name.test.ts"

NAME="$name" DESC="$description" python3 - <<'PY'
import json, os, pathlib
name, desc = os.environ["NAME"], os.environ["DESC"]
for path in pathlib.Path(name).rglob("*"):
    if path.suffix in {".json", ".ts", ".tsx"}:
        path.write_bytes(path.read_bytes().replace(b"mod-template", name.encode()))
manifest = pathlib.Path(name, ".claude-plugin", "plugin.json")
plugin = json.loads(manifest.read_text(encoding="utf-8"))
plugin["description"] = desc
manifest.write_bytes((json.dumps(plugin, indent=2, ensure_ascii=False) + "\n").encode())
market = pathlib.Path(".claude-plugin", "marketplace.json")
data = json.loads(market.read_text(encoding="utf-8"))
data["plugins"].append({"name": name, "source": f"./{name}", "description": desc})
market.write_bytes((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode())
PY

claude plugin validate "$name"
claude plugin test "$name"
echo "Created $name/. Run it live with: claude --plugin-dir \"$PWD/$name\""
