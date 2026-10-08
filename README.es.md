# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Español** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**Elegidos a mano, validados y fijados. Una sola adición, 43 mods.**

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

### Paneles y uso

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>de hamzafer</sub> | Una línea bajo la barra de estado: minutos de caché caliente que quedan y cuántos tokens volverá a cachear el próximo mensaje | archivos, ejecuta comandos |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>de hamzafer</sub> | La ventana de contexto como barra apilada con un color por categoría, tokens y punto de compactación (/context-bar) | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>de hamzafer</sub> | Saldo estimado de la API de OpenAI, gasto de hoy y en qué se fue (/openai-balance) | red, ejecuta comandos |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>de hamzafer</sub> | El uso del contexto como parte meteorológico, con la cuenta atrás de la caché del prompt | archivos, ejecuta comandos |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>de hamzafer</sub> | Uso de 5 horas y 7 días en barras pequeñas, con cuenta atrás del reinicio y coste de la sesión | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>de JetsonChan</sub> | Límites de 5 horas y 7 días, contexto y aciertos de caché sobre el prompt, para terminal y app de escritorio | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>de kongyo2</sub> | El contexto en una fila, dibujado como los medidores propios de Claude Code, con lo que queda hasta la compactación automática | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>de scasella</sub> | Panel de agentes: estado del modelo, cada decisión de permisos, tarjetas y carriles de subagentes, recibo del turno y registro de la sesión | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>de tomstagl</sub> | Panel en vivo estilo btop: contexto, tokens, coste, aciertos de caché, límites y latencia por herramienta (/cctop) | archivos, ejecuta comandos |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>de xuanji86</sub> | Tarjeta de estado flotante sobre el prompt: modelo, effort, contexto, límites de 5 h y semanales, coste, rama y CI | archivos, ejecuta comandos |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>de zycck</sub> | Barras de progreso del plan sobre el prompt: etapas, pasos, relleno pixelado y sonidos suaves al decidir, fallar y terminar | archivos, ejecuta comandos |

### Agentes y subagentes

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>de Charlie0113-T</sub> | /flow abre junto a la conversación un árbol en vivo de subagentes y compañeros | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>de hamzafer</sub> | Una línea por subagente en marcha: tiempo, número de herramientas y qué hace (/radar muestra todos) | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>de hamzafer</sub> | Muestra quién tiene el navegador Playwright; los subagentes esperan turno y /browser clean cierra los restos | ejecuta comandos |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>de hamzafer</sub> | /mission abre un mapa en vivo del agente principal, sus subagentes y cada llamada a herramientas, más un mapa de archivos | archivos, llama a modelos, ejecuta comandos |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>de hamzafer</sub> | Una línea en vivo por cada revisión de código (Codex o subagente revisor) y un aviso con los hallazgos al terminar | ejecuta comandos |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>de hamzafer</sub> | Elige modelo para los subagentes que no lo indican (OpenAI Decisions API o Jev); /route muestra elecciones y costes | red |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>de xuanji86</sub> | Panel lateral con los subagentes: qué hace cada uno, cuántos tokens gasta y su conversación a un clic | — |

### Productividad y contexto

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>de hamzafer</sub> | Lo que te espera en una línea: próxima reunión, PR, issues de Linear y mensajes de Slack (vía MCP conectado) | MCP, ejecuta comandos |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>de hamzafer</sub> | Tras cada turno, 2 o 3 posibles siguientes prompts; pulsa 1, 2 o 3 con el prompt vacío para usarlos | llama a modelos |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>de hamzafer</sub> | Pone nombre a las sesiones sin título; /park guarda dónde lo dejaste y lo muestra al reanudar | llama a modelos, ejecuta comandos |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>de hamzafer</sub> | Resumen en vivo sobre el prompt: objetivo, qué hace ahora, qué espera de ti y siguiente paso (/where amplía) | llama a modelos |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>de JayDoubleu</sub> | Chat lateral de solo lectura: /aside para preguntar sobre la sesión sin escribir nada en el hilo principal | llama a modelos |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>de lossless-claude</sub> | Gestión de contexto sin pérdidas: resúmenes en un DAG que mantienen accesible cada mensaje | archivos, red, llama a modelos, ejecuta comandos |

### Renderizado y vistas previas

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>de briangtn</sub> | Markdown al estilo GitHub en la conversación: avisos, listas de tareas, tachado y diagramas Mermaid | ejecuta comandos |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>de hamzafer</sub> | Los Markdown que edita Claude, renderizados como en GitHub en un panel lateral, con antes y después (/md) | archivos, ejecuta comandos |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>de hamzafer</sub> | Repasa las ediciones de archivos del último turno, un diff cada vez | archivos |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>de hellosverre</sub> | Temas para la conversación: filas de herramientas, márgenes de respuesta y textos del spinner; /skin los cambia al momento | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>de xuanji86</sub> | Haz clic en una ruta .md de la conversación para leerla renderizada al lado, con imágenes, y señala un bloque para que Claude lo edite | archivos, ejecuta comandos |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>de zenbu-labs</sub> | Un navegador junto a la conversación: vista previa de sitios web y HTML local, y el agente también puede manejarlo | archivos, red, ejecuta comandos |

### Seguridad y protecciones

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>de hamzafer</sub> | Detiene los comandos Bash arriesgados y muestra qué cambiarían antes de que confirmes | ejecuta comandos |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>de hamzafer</sub> | Retiene `gh pr merge` hasta que pase la CI y se haya hecho una revisión con Codex | archivos, ejecuta comandos |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>de hamzafer</sub> | Reglas de escritura y git: cambia las rayas en prosa y pregunta antes de un amend, un push sin formatear o datos personales en commits | archivos, ejecuta comandos |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>de ray-amjad</sub> | Cambia secretos, correos e IPs por marcadores fijos antes de que lleguen a la conversación, y los restaura al llamar herramientas | — |

### Git, PR y despliegues

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>de ray-amjad</sub> | La cola de despliegues de Vercel del proyecto vinculado, fija bajo el prompt, con fase y tiempo | archivos, ejecuta comandos |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>de sezaakgun</sub> | Estado de fusión, revisiones y checks obligatorios de los PR de GitHub que sigues, con aviso cuando cambian | archivos, ejecuta comandos |

### Mientras esperas

| Mod | Qué hace | Acceso |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>de darrell-tw</sub> | Panel de acciones de Taiwán y EE. UU. que cambia según el horario de mercado, con modo de pérdidas y ganancias | archivos, red, ejecuta comandos |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>de halluton</sub> | Ejercicios de respiración guiados sobre el prompt mientras Claude trabaja; el spinner cuenta contigo | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>de hamzafer</sub> | Lo que suena en Spotify en una línea: canción, progreso y letra actual, con botones (solo macOS) | red, ejecuta comandos |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>de hamzafer</sub> | La oración actual, la siguiente y el tiempo que falta, calculados en tu equipo sin enviar nada | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>de hamzafer</sub> | YouTube Shorts en un panel del terminal: se reproducen mientras Claude trabaja y se pausan al terminar | archivos, red, ejecuta comandos |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>de hamzafer</sub> | La serpiente en un panel mientras Claude trabaja; no aparece hasta que escribes /snake | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>de sezaakgun</sub> | Nueve juegos sobre el prompt (serpiente, bloques, 2048…) y una mascota que crece con tests y commits | — |

## Sugerir un mod

Abre un issue con el enlace al repositorio del mod. Para añadirlo tú mismo, agrega una entrada en `community.json` (repositorio, carpeta, commit revisado, categoría y licencia), escribe sus resúmenes de una línea en `readme/summaries.json`, ejecuta `python3 scripts/build-catalog.py` y abre un pull request.

## Créditos

Cada mod pertenece a su autor y conserva su propia licencia; este repositorio solo los enumera. Muchos se encontraron gracias a [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods). Los autores que quieran cambiar o retirar una entrada pueden abrir un issue.

Proyecto no oficial; no es un producto de Anthropic.
