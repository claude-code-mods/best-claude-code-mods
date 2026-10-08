# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Português (Brasil)** · [Русский](README.ru.md)

**Escolhidos a dedo, validados e fixados. Uma adição, 43 mods.**

Mods são plugins do Claude Code feitos de hooks de função: observam, alteram ou respondem ao que o Claude Code faz, e desenham a própria interface. Este marketplace reúne os melhores mods da comunidade. Cada um foi verificado com `claude plugin validate` e fixado no commit verificado, então mudanças posteriores do autor nunca chegam até você sem revisão.

Requer Claude Code 2.1.287 ou mais recente.

## Instalação

Numa sessão do Claude Code no terminal:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

Por exemplo `/plugin install terminal-browser@best-claude-code-mods`. Rode `/plugin marketplace update best-claude-code-mods` para receber mods novos e atualizações.

## Catálogo

A coluna **Acesso** mostra o que, segundo o validador, o código do mod pode fazer além de desenhar a interface. Leia o código de um mod antes de instalá-lo: a validação lê o código sem executá-lo e não é uma auditoria de segurança.

### Painéis e uso

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>por hamzafer</sub> | Uma linha sob a barra de status: minutos de cache ainda quente e quantos tokens a próxima mensagem vai recachear | arquivos, executa comandos |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>por hamzafer</sub> | A janela de contexto como barra empilhada, uma cor por categoria, com tokens e ponto de compactação (/context-bar) | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>por hamzafer</sub> | Saldo estimado da API da OpenAI, gasto de hoje e para onde foi (/openai-balance) | rede, executa comandos |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>por hamzafer</sub> | O uso do contexto como previsão do tempo, com contagem regressiva do cache do prompt | arquivos, executa comandos |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>por hamzafer</sub> | Uso de 5 horas e 7 dias em barrinhas, com contagem até o reset e custo da sessão | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>por JetsonChan</sub> | Limites de 5 horas e 7 dias, contexto e acertos de cache acima do prompt, no terminal e no app desktop | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>por kongyo2</sub> | O contexto numa linha, desenhado como os medidores do próprio Claude Code, com o que falta até a compactação automática | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>por scasella</sub> | Painel de agentes: estado do modelo, cada decisão de permissão, cartões e raias de subagentes, recibo do turno e log da sessão | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>por tomstagl</sub> | Painel ao vivo estilo btop: contexto, tokens, custo, acertos de cache, limites e latência por ferramenta (/cctop) | arquivos, executa comandos |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>por xuanji86</sub> | Cartão de status flutuante acima do prompt: modelo, effort, contexto, limites de 5 h e semanal, custo, branch e CI | arquivos, executa comandos |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>por zycck</sub> | Barras de progresso do plano acima do prompt: etapas, passos, preenchimento em pixel e sons suaves para decisão, erro e fim | arquivos, executa comandos |

### Agentes e subagentes

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>por Charlie0113-T</sub> | /flow abre ao lado da conversa uma árvore ao vivo dos subagentes e colegas | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>por hamzafer</sub> | Uma linha por subagente em execução: tempo, número de ferramentas e o que está fazendo (/radar mostra todos) | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>por hamzafer</sub> | Mostra quem está com o navegador Playwright; subagentes esperam a vez e /browser clean fecha os restos | executa comandos |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>por hamzafer</sub> | /mission abre um mapa ao vivo do agente principal, subagentes e cada chamada de ferramenta, além de um mapa dos arquivos | arquivos, chama modelos, executa comandos |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>por hamzafer</sub> | Uma linha ao vivo para cada revisão de código (Codex ou subagente revisor) e um aviso com os achados no fim | executa comandos |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>por hamzafer</sub> | Escolhe o modelo dos subagentes que não indicam um (OpenAI Decisions API ou Jev); /route mostra escolhas e custos | rede |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>por xuanji86</sub> | Painel lateral com os subagentes: o que cada um faz, quantos tokens gasta e a conversa a um clique | — |

### Produtividade e contexto

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>por hamzafer</sub> | O que precisa de você numa linha: próxima reunião, PRs, issues do Linear e DMs do Slack (via MCP conectado) | MCP, executa comandos |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>por hamzafer</sub> | Depois de cada turno, 2 ou 3 próximos prompts prováveis; tecle 1, 2 ou 3 com o prompt vazio para usar | chama modelos |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>por hamzafer</sub> | Dá nome às sessões sem título; /park salva onde você parou e mostra ao retomar | chama modelos, executa comandos |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>por hamzafer</sub> | Resumo ao vivo acima do prompt: objetivo, o que faz agora, o que espera de você e próximo passo (/where detalha) | chama modelos |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>por JayDoubleu</sub> | Chat lateral somente leitura: /aside para perguntar sobre a sessão sem escrever nada na conversa principal | chama modelos |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>por lossless-claude</sub> | Gestão de contexto sem perdas: resumos num DAG que mantêm cada mensagem acessível | arquivos, rede, chama modelos, executa comandos |

### Renderização e pré-visualização

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>por briangtn</sub> | Markdown no estilo GitHub na conversa: alertas, listas de tarefas, tachado e diagramas Mermaid | executa comandos |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>por hamzafer</sub> | Os Markdown que o Claude edita, renderizados como no GitHub num painel lateral, com antes e depois (/md) | arquivos, executa comandos |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>por hamzafer</sub> | Repasse as edições de arquivos do último turno, um diff de cada vez | arquivos |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>por hellosverre</sub> | Temas para a conversa: linhas de ferramentas, margens das respostas e textos do spinner; /skin troca na hora | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>por xuanji86</sub> | Clique num caminho .md da conversa para lê-lo renderizado ao lado, com imagens, e aponte um bloco para o Claude editar | arquivos, executa comandos |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>por zenbu-labs</sub> | Um navegador ao lado da conversa: pré-visualize sites e HTML local, e deixe o agente controlá-lo | arquivos, rede, executa comandos |

### Segurança e proteções

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>por hamzafer</sub> | Segura comandos Bash arriscados e mostra o que mudariam antes de você confirmar | executa comandos |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>por hamzafer</sub> | Segura `gh pr merge` até a CI passar e uma revisão do Codex ter rodado | arquivos, executa comandos |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>por hamzafer</sub> | Regras de escrita e git: troca travessões no texto e pergunta antes de amend, push sem formatar ou dados pessoais em commits | arquivos, executa comandos |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>por ray-amjad</sub> | Troca segredos, e-mails e IPs por marcadores fixos antes de entrarem na conversa e os restaura nas chamadas de ferramentas | — |

### Git, PRs e deploys

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>por ray-amjad</sub> | A fila de deploys da Vercel do projeto vinculado, fixa sob o prompt, com fase e tempo | arquivos, executa comandos |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>por sezaakgun</sub> | Estado de merge, revisões e checks obrigatórios dos PRs do GitHub que você acompanha, com alerta quando mudam | arquivos, executa comandos |

### Enquanto você espera

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | O que faz | Acesso |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>por darrell-tw</sub> | Painel de ações de Taiwan e dos EUA que alterna conforme o pregão, com modo de lucros e perdas | arquivos, rede, executa comandos |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>por halluton</sub> | Exercícios de respiração guiados acima do prompt enquanto o Claude trabalha; o spinner conta com você | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>por hamzafer</sub> | O que toca no Spotify numa linha: faixa, progresso e letra atual, com botões (só macOS) | rede, executa comandos |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>por hamzafer</sub> | A oração atual, a próxima e quanto falta, calculadas no seu computador sem enviar nada | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>por hamzafer</sub> | YouTube Shorts num painel do terminal: tocam enquanto o Claude trabalha e pausam ao terminar | arquivos, rede, executa comandos |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>por hamzafer</sub> | Jogo da cobrinha num painel enquanto o Claude trabalha; só abre com /snake | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>por sezaakgun</sub> | Nove jogos acima do prompt (cobrinha, blocos, 2048…) e um bichinho que cresce com testes e commits | — |

## Sugerir um mod

Abra uma issue com o link do repositório do mod. Para adicioná-lo você mesmo, inclua uma entrada em `community.json` (repositório, pasta, commit revisado, categoria e licença), escreva os resumos de uma linha em `readme/summaries.json`, rode `python3 scripts/build-catalog.py` e abra um pull request.

## Créditos

Cada mod pertence ao seu autor e mantém a própria licença; este repositório apenas os lista. Autores que queiram alterar ou remover uma entrada podem abrir uma issue.

Projeto não oficial; não é um produto da Anthropic.
