# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**Handverlesen, geprüft, festgepinnt. Einmal hinzufügen, 43 Mods.**

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

### Dashboards und Verbrauch

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>von hamzafer</sub> | Eine Zeile unter der Statuszeile: Minuten, die der Prompt-Cache noch warm ist, und wie viele Tokens danach neu gecacht werden | Dateien, führt Befehle aus |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>von hamzafer</sub> | Das Kontextfenster als gestapelter Balken, eine Farbe pro Kategorie, mit Tokens und Verdichtungspunkt (/context-bar) | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>von hamzafer</sub> | Geschätztes OpenAI-API-Guthaben, heutige Ausgaben und wofür (/openai-balance) | Netzwerk, führt Befehle aus |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>von hamzafer</sub> | Die Kontextauslastung als Wetterbericht, mit Countdown für den Prompt-Cache | Dateien, führt Befehle aus |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>von hamzafer</sub> | 5-Stunden- und 7-Tage-Verbrauch als kleine Balken, mit Countdown bis zum Reset und Sitzungskosten | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>von JetsonChan</sub> | 5-Stunden- und 7-Tage-Limits, Kontext und Cache-Trefferquote über dem Prompt, im Terminal und in der Desktop-App | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>von kongyo2</sub> | Der Kontext in einer Zeile, gezeichnet wie Claude Codes eigene Anzeigen, mit dem Rest bis zur automatischen Verdichtung | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>von scasella</sub> | Agenten-Dashboard: Modellstatus, jede Berechtigungsentscheidung, Subagenten-Karten und Swimlanes, Beleg pro Durchgang und Sitzungsprotokoll | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>von tomstagl</sub> | Live-Dashboard im btop-Stil: Kontext, Tokens, Kosten, Cache-Trefferquote, Limits und Latenz pro Werkzeug (/cctop) | Dateien, führt Befehle aus |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>von xuanji86</sub> | Schwebende Statuskarte über dem Prompt: Modell, Effort, Kontext, 5-Stunden- und Wochenlimit, Kosten, Branch und CI | Dateien, führt Befehle aus |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>von zycck</sub> | Fortschrittsbalken des Plans über dem Prompt: Phasen, Schritte, Pixelfüllung und leise Töne bei Entscheidung, Fehler und Abschluss | Dateien, führt Befehle aus |

### Agenten und Subagenten

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>von Charlie0113-T</sub> | /flow öffnet neben dem Gespräch einen Live-Baum der Subagenten und Teammitglieder | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>von hamzafer</sub> | Eine Zeile pro laufendem Subagenten: Zeit, Werkzeuganzahl und was er tut (/radar zeigt alle) | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>von hamzafer</sub> | Zeigt, wer den Playwright-Browser hält; Subagenten warten, /browser clean schließt übrig gebliebene Browser | führt Befehle aus |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>von hamzafer</sub> | /mission öffnet eine Live-Karte von Hauptagent, Subagenten und jedem Werkzeugaufruf, dazu eine Karte der berührten Dateien | Dateien, ruft Modelle auf, führt Befehle aus |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>von hamzafer</sub> | Eine Live-Zeile pro laufendem Code-Review (Codex oder Review-Subagent), am Ende eine Meldung mit den Befunden | führt Befehle aus |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>von hamzafer</sub> | Wählt das Modell für Subagenten ohne Angabe (OpenAI Decisions API oder Jev); /route zeigt Wahl und Kosten | Netzwerk |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>von xuanji86</sub> | Seitenbereich mit den Subagenten: was jeder tut, was er an Tokens kostet, sein Gespräch einen Klick entfernt | — |

### Produktivität und Kontext

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>von hamzafer</sub> | Was auf dich wartet in einer Zeile: nächstes Meeting, PRs, Linear-Issues und Slack-DMs (über verbundenes MCP) | MCP, führt Befehle aus |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>von hamzafer</sub> | Nach jedem Durchgang 2 bis 3 wahrscheinliche nächste Prompts; 1, 2 oder 3 im leeren Prompt übernimmt einen | ruft Modelle auf |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>von hamzafer</sub> | Benennt unbenannte Sitzungen; /park merkt sich den Stand und zeigt ihn beim Fortsetzen | ruft Modelle auf, führt Befehle aus |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>von hamzafer</sub> | Live-Zusammenfassung über dem Prompt: Ziel, aktueller Schritt, was auf dich wartet, nächster Schritt (/where ausführlich) | ruft Modelle auf |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>von JayDoubleu</sub> | Nur lesender Nebenchat: /aside fragt zur laufenden Sitzung, ohne etwas in den Hauptverlauf zu schreiben | ruft Modelle auf |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>von lossless-claude</sub> | Verlustfreie Kontextverwaltung: Zusammenfassungen als DAG, jede Nachricht bleibt erreichbar | Dateien, Netzwerk, ruft Modelle auf, führt Befehle aus |

### Darstellung und Vorschau

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>von briangtn</sub> | GitHub-Markdown im Gespräch: Hinweisblöcke, Aufgabenlisten, Durchstreichungen und Mermaid-Diagramme | führt Befehle aus |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>von hamzafer</sub> | Von Claude bearbeitete Markdown-Dateien wie auf GitHub gerendert im Seitenbereich, vorher und nachher (/md) | Dateien, führt Befehle aus |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>von hamzafer</sub> | Die Dateiänderungen des letzten Durchgangs Diff für Diff durchgehen | Dateien |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>von hellosverre</sub> | Skins für das Gesprächsprotokoll: Werkzeugzeilen, Antwortränder und Spinner-Texte; /skin wechselt sofort | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>von xuanji86</sub> | Auf einen .md-Pfad im Gespräch klicken und die Datei gerendert daneben lesen, mit Bildern; einen Block zeigen, den Claude ändern soll | Dateien, führt Befehle aus |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>von zenbu-labs</sub> | Ein Browser neben dem Gespräch: Websites und lokales HTML ansehen, auch vom Agenten steuerbar | Dateien, Netzwerk, führt Befehle aus |

### Sicherheit und Schutz

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>von hamzafer</sub> | Hält riskante Bash-Befehle an und zeigt vor deiner Bestätigung, was sie ändern würden | führt Befehle aus |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>von hamzafer</sub> | Hält `gh pr merge` zurück, bis die CI grün ist und ein Codex-Review gelaufen ist | Dateien, führt Befehle aus |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>von hamzafer</sub> | Schreib- und Git-Regeln: ersetzt Gedankenstriche, fragt vor amend, unformatiertem Push oder persönlichen Daten in Commits | Dateien, führt Befehle aus |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>von ray-amjad</sub> | Ersetzt Geheimnisse, E-Mails und IPs durch feste Platzhalter, bevor sie ins Gespräch gelangen, und setzt sie bei Werkzeugaufrufen zurück | — |

### Git, PRs und Deployments

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>von ray-amjad</sub> | Die Vercel-Deploy-Warteschlange des verknüpften Projekts unter dem Prompt, mit Phase und Dauer | Dateien, führt Befehle aus |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>von sezaakgun</sub> | Merge-Status, Reviews und Pflicht-Checks beobachteter GitHub-PRs, mit Hinweis bei Änderungen | Dateien, führt Befehle aus |

### Während du wartest

| Mod | Was er tut | Zugriff |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>von darrell-tw</sub> | Watchlist für taiwanische und US-Aktien je nach Handelszeit, mit Gewinn-und-Verlust-Ansicht | Dateien, Netzwerk, führt Befehle aus |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>von halluton</sub> | Geführte Atemübungen über dem Prompt, während Claude arbeitet; der Spinner zählt mit | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>von hamzafer</sub> | Was Spotify spielt, in einer Zeile: Titel, Fortschritt und aktuelle Liedzeile, mit Tasten (nur macOS) | Netzwerk, führt Befehle aus |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>von hamzafer</sub> | Aktuelles und nächstes Gebet mit Restzeit, lokal aus deinem Standort berechnet, ohne etwas zu senden | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>von hamzafer</sub> | YouTube Shorts in einem Terminalbereich: laufen, während Claude arbeitet, und pausieren danach | Dateien, Netzwerk, führt Befehle aus |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>von hamzafer</sub> | Snake in einem Bereich, während Claude arbeitet; erscheint erst nach /snake | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>von sezaakgun</sub> | Neun Spiele über dem Prompt (Snake, Blöcke, 2048 …) und ein Haustier, das mit Tests und Commits wächst | — |

## Einen Mod vorschlagen

Öffne ein Issue mit dem Link zum Repository des Mods. Um ihn selbst hinzuzufügen, ergänze einen Eintrag in `community.json` (Repository, Ordner, geprüfter Commit, Kategorie, Lizenz), schreibe seine Einzeiler in `readme/summaries.json`, führe `python3 scripts/build-catalog.py` aus und öffne einen Pull Request.

## Danksagung

Jeder Mod gehört seinem Autor und behält seine eigene Lizenz; dieses Repository listet sie nur auf. Viele wurden über [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods) gefunden. Autoren, die einen Eintrag ändern oder entfernen lassen möchten, können ein Issue öffnen.

Inoffiziell; kein Produkt von Anthropic.
