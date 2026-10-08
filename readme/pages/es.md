# Best Claude Code Mods

{{languages}}

**Elegidos a mano, validados y fijados. Una sola adición, {{count}} mods.**

Los mods son plugins de Claude Code hechos con hooks de funciones: observan, cambian o responden a lo que hace Claude Code, y dibujan su propia interfaz. Este marketplace reúne los mejores mods de la comunidad. Cada uno se ha comprobado con `claude plugin validate` y está fijado al commit comprobado, así que los cambios posteriores de su autor nunca te llegan sin revisar.

Requiere Claude Code 2.1.287 o posterior.

## Instalación

En una sesión de Claude Code en el terminal:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

Por ejemplo `/plugin install terminal-browser@best-claude-code-mods`. Ejecuta `/plugin marketplace update best-claude-code-mods` para recibir mods nuevos y actualizaciones.

## Catálogo

La columna **Acceso** indica lo que, según el validador, puede hacer el código del mod además de dibujar interfaz. Lee el código de un mod antes de instalarlo: la validación lo lee sin ejecutarlo y no es una auditoría de seguridad.

{{catalog}}

## Sugerir un mod

Abre un issue con el enlace al repositorio del mod. Para añadirlo tú mismo, agrega una entrada en `community.json` (repositorio, carpeta, commit revisado, categoría y licencia), escribe sus resúmenes de una línea en `readme/summaries.json`, ejecuta `python3 scripts/build-catalog.py` y abre un pull request.

## Créditos

Cada mod pertenece a su autor y conserva su propia licencia; este repositorio solo los enumera. Los autores que quieran cambiar o retirar una entrada pueden abrir un issue.

Proyecto no oficial; no es un producto de Anthropic.
