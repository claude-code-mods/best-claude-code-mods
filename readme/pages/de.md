# Best Claude Code Mods

{{languages}}

**Handverlesen, geprüft, festgepinnt. Einmal hinzufügen, {{count}} Mods.**

Mods sind Claude-Code-Plugins aus Funktions-Hooks: Sie beobachten, ändern oder übernehmen, was Claude Code tut, und zeichnen ihre eigene Oberfläche. Dieser Marketplace sammelt die besten Mods der Community. Jeder ist mit `claude plugin validate` geprüft und auf den geprüften Commit festgelegt, sodass spätere Änderungen des Autors dich nie ungeprüft erreichen.

Erfordert Claude Code 2.1.287 oder neuer.

## Installation

In einer Claude-Code-Sitzung im Terminal:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

Zum Beispiel `/plugin install terminal-browser@best-claude-code-mods`. Mit `/plugin marketplace update best-claude-code-mods` holst du neue Mods und Updates.

## Katalog

Die Spalte **Zugriff** zeigt, was der Code eines Mods laut Validator über das Zeichnen der Oberfläche hinaus tun kann. Lies den Quellcode eines Mods, bevor du ihn installierst: Die Prüfung liest den Code, ohne ihn auszuführen, und ist kein Sicherheitsaudit.

{{catalog}}

## Einen Mod vorschlagen

Öffne ein Issue mit dem Link zum Repository des Mods. Um ihn selbst hinzuzufügen, ergänze einen Eintrag in `community.json` (Repository, Ordner, geprüfter Commit, Kategorie, Lizenz), schreibe seine Einzeiler in `readme/summaries.json`, führe `python3 scripts/build-catalog.py` aus und öffne einen Pull Request.

## Danksagung

Jeder Mod gehört seinem Autor und behält seine eigene Lizenz; dieses Repository listet sie nur auf. Autoren, die einen Eintrag ändern oder entfernen lassen möchten, können ein Issue öffnen.

Inoffiziell; kein Produkt von Anthropic.
