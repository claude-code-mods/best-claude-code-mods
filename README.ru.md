# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · **Русский**

**Отобраны вручную, проверены, версии закреплены. Одно добавление — 43 модов.**

Моды — это плагины Claude Code на функциональных хуках: они наблюдают за действиями Claude Code, меняют их или отвечают вместо него и рисуют собственный интерфейс. В этом маркетплейсе собраны лучшие моды сообщества. Каждый проверен командой `claude plugin validate` и закреплён на проверенном коммите, поэтому последующие изменения автора не попадут к вам без проверки.

Нужен Claude Code 2.1.287 или новее.

## Установка

В сессии Claude Code в терминале:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <мод>@best-claude-code-mods
```

Например, `/plugin install terminal-browser@best-claude-code-mods`. Чтобы получить новые моды и обновления, выполните `/plugin marketplace update best-claude-code-mods`.

## Каталог

Столбец **Доступ** показывает, что, по данным валидатора, код мода может делать помимо отрисовки интерфейса. Прочитайте исходный код мода перед установкой: проверка читает код, не запуская его, и не является аудитом безопасности.

### Панели и расход

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>автор hamzafer</sub> | Строка под строкой состояния: сколько минут кэш ещё «тёплый» и сколько токенов придётся кэшировать заново | файлы, запуск команд |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>автор hamzafer</sub> | Окно контекста в виде составной полосы, цвет на категорию, с числом токенов и точкой сжатия (/context-bar) | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>автор hamzafer</sub> | Оценка баланса OpenAI API, траты за сегодня и на что ушли деньги (/openai-balance) | сеть, запуск команд |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>автор hamzafer</sub> | Заполнение контекста в виде прогноза погоды, с обратным отсчётом кэша промпта | файлы, запуск команд |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>автор hamzafer</sub> | Расход за 5 часов и 7 дней маленькими полосками, с отсчётом до сброса и стоимостью сессии | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>автор JetsonChan</sub> | Лимиты на 5 часов и 7 дней, контекст и попадания в кэш над полем ввода, в терминале и в настольном приложении | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>автор kongyo2</sub> | Контекст одной строкой, в стиле встроенных индикаторов Claude Code, с остатком до автосжатия | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>автор scasella</sub> | Панель агентов: состояние модели, каждое решение о разрешениях, карточки и дорожки субагентов, «чек» хода и журнал сессии | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>автор tomstagl</sub> | Живая панель в стиле btop: контекст, токены, стоимость, попадания в кэш, лимиты и задержки по инструментам (/cctop) | файлы, запуск команд |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>автор xuanji86</sub> | Плавающая карточка состояния над полем ввода: модель, effort, контекст, лимиты на 5 часов и неделю, стоимость, ветка и CI | файлы, запуск команд |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>автор zycck</sub> | Полосы прогресса плана над полем ввода: этапы, шаги, пиксельная заливка и тихие звуки при решении, ошибке и завершении | файлы, запуск команд |

### Агенты и субагенты

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>автор Charlie0113-T</sub> | /flow открывает рядом с диалогом живое дерево субагентов и участников команды | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>автор hamzafer</sub> | По строке на каждого работающего субагента: время, число вызовов инструментов, чем занят (/radar — все) | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>автор hamzafer</sub> | Показывает, кто занял браузер Playwright; субагенты ждут очереди, /browser clean закрывает оставшиеся | запуск команд |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>автор hamzafer</sub> | /mission открывает живую карту главного агента, субагентов и всех вызовов инструментов, плюс карту затронутых файлов | файлы, вызов моделей, запуск команд |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>автор hamzafer</sub> | Живая строка для каждого идущего ревью кода (Codex или субагент-ревьюер), по завершении — уведомление с выводами | запуск команд |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>автор hamzafer</sub> | Подбирает модель субагентам, у которых она не указана (OpenAI Decisions API или Jev); /route — выбор и стоимость | сеть |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>автор xuanji86</sub> | Боковая панель субагентов: чем занят каждый, сколько токенов тратит, его диалог в один клик | — |

### Продуктивность и контекст

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>автор hamzafer</sub> | Всё, что ждёт вас, одной строкой: следующая встреча, PR, задачи Linear и личные сообщения Slack (через MCP) | MCP, запуск команд |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>автор hamzafer</sub> | После каждого хода 2–3 вероятных следующих запроса; нажмите 1, 2 или 3 в пустом поле, чтобы взять один | вызов моделей |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>автор hamzafer</sub> | Даёт имена безымянным сессиям; /park запоминает, где вы остановились, и показывает это при возобновлении | вызов моделей, запуск команд |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>автор hamzafer</sub> | Живая сводка над полем ввода: цель, что делается сейчас, что ждёт вас, следующий шаг (/where — подробнее) | вызов моделей |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>автор JayDoubleu</sub> | Боковой чат только для чтения: /aside — вопросы о текущей сессии, ничего не пишется в основную ветку | вызов моделей |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>автор lossless-claude</sub> | Управление контекстом без потерь: сводки в виде DAG, каждое сообщение остаётся доступным | файлы, сеть, вызов моделей, запуск команд |

### Отображение и просмотр

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>автор briangtn</sub> | Markdown в стиле GitHub в диалоге: блоки-подсказки, списки задач, зачёркивание и диаграммы Mermaid | запуск команд |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>автор hamzafer</sub> | Markdown-файлы, которые правит Claude, в боковой панели как на GitHub, «до» и «после» рядом (/md) | файлы, запуск команд |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>автор hamzafer</sub> | Пошаговый просмотр правок файлов за последний ход, по одному diff | файлы |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>автор hellosverre</sub> | Темы оформления диалога: строки инструментов, поля ответов и надписи спиннера; /skin переключает на лету | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>автор xuanji86</sub> | Щёлкните путь к .md в диалоге, чтобы читать файл рядом в отрисованном виде с картинками, и укажите блок, который Claude должен изменить | файлы, запуск команд |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>автор zenbu-labs</sub> | Браузер рядом с диалогом: просмотр сайтов и локального HTML, агент тоже может им управлять | файлы, сеть, запуск команд |

### Безопасность и защита

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>автор hamzafer</sub> | Задерживает опасные команды Bash и показывает, что они изменят, прежде чем вы подтвердите | запуск команд |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>автор hamzafer</sub> | Не пускает `gh pr merge`, пока не пройдёт CI и не будет выполнено ревью Codex | файлы, запуск команд |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>автор hamzafer</sub> | Правила текста и git: заменяет длинные тире и спрашивает перед amend, неотформатированным push или личными данными в коммитах | файлы, запуск команд |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>автор ray-amjad</sub> | Заменяет секреты, адреса почты и IP постоянными заглушками до попадания в диалог и возвращает их при вызове инструментов | — |

### Git, PR и деплой

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>автор ray-amjad</sub> | Очередь деплоев Vercel связанного проекта под полем ввода, с этапом и временем | файлы, запуск команд |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>автор sezaakgun</sub> | Состояние слияния, ревью и обязательные проверки отслеживаемых PR на GitHub, с оповещением при изменениях | файлы, запуск команд |

### Пока ждёте

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Что делает | Доступ |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>автор darrell-tw</sub> | Список акций Тайваня и США, переключается по торговым часам, с режимом прибылей и убытков | файлы, сеть, запуск команд |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>автор halluton</sub> | Дыхательные упражнения над полем ввода, пока Claude работает; спиннер считает вместе с вами | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>автор hamzafer</sub> | Что играет в Spotify, одной строкой: трек, прогресс и текущая строка песни, с кнопками (только macOS) | сеть, запуск команд |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>автор hamzafer</sub> | Текущая и следующая молитва и оставшееся время, считаются локально по вашему местоположению | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>автор hamzafer</sub> | YouTube Shorts в панели терминала: играют, пока Claude работает, и встают на паузу по завершении | файлы, сеть, запуск команд |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>автор hamzafer</sub> | «Змейка» в панели, пока Claude работает; появляется только после /snake | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>автор sezaakgun</sub> | Девять игр над полем ввода («змейка», блоки, 2048…) и питомец, который растёт от тестов и коммитов | — |

## Предложить мод

Откройте issue со ссылкой на репозиторий мода. Чтобы добавить его самостоятельно, внесите запись в `community.json` (репозиторий, папка, проверенный коммит, категория, лицензия), напишите однострочные описания в `readme/summaries.json`, запустите `python3 scripts/build-catalog.py` и откройте pull request.

## Благодарности

Каждый мод принадлежит своему автору и распространяется под его лицензией; этот репозиторий только собирает их. Авторы, желающие изменить или убрать запись, могут открыть issue.

Неофициальный проект; не является продуктом Anthropic.
