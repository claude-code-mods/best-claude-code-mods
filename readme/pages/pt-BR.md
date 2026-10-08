# Best Claude Code Mods

{{languages}}

**Escolhidos a dedo, validados e fixados. Uma adição, {{count}} mods.**

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

{{catalog}}

## Sugerir um mod

Abra uma issue com o link do repositório do mod. Para adicioná-lo você mesmo, inclua uma entrada em `community.json` (repositório, pasta, commit revisado, categoria e licença), escreva os resumos de uma linha em `readme/summaries.json`, rode `python3 scripts/build-catalog.py` e abra um pull request.

## Créditos

Cada mod pertence ao seu autor e mantém a própria licença; este repositório apenas os lista. Autores que queiram alterar ou remover uma entrada podem abrir uma issue.

Projeto não oficial; não é um produto da Anthropic.
