# Best Claude Code Mods

{{languages}}

**Choisis à la main, validés, épinglés. Un seul ajout, {{count}} mods.**

Les mods sont des plugins Claude Code faits de hooks de fonctions : ils observent, modifient ou prennent en charge ce que fait Claude Code, et dessinent leur propre interface. Ce marketplace rassemble les meilleurs mods de la communauté. Chacun est vérifié avec `claude plugin validate` et épinglé au commit vérifié : les modifications ultérieures de son auteur ne vous parviennent jamais sans relecture.

Nécessite Claude Code 2.1.287 ou plus récent.

## Installation

Dans une session Claude Code au terminal :

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

Par exemple `/plugin install terminal-browser@best-claude-code-mods`. Lancez `/plugin marketplace update best-claude-code-mods` pour recevoir les nouveaux mods et les mises à jour.

## Catalogue

La colonne **Accès** indique ce que, selon le validateur, le code du mod peut faire en plus de dessiner son interface. Lisez le code d'un mod avant de l'installer : la validation le lit sans l'exécuter et ne constitue pas un audit de sécurité.

{{catalog}}

## Proposer un mod

Ouvrez une issue avec le lien vers le dépôt du mod. Pour l'ajouter vous-même, ajoutez une entrée dans `community.json` (dépôt, dossier, commit relu, catégorie, licence), écrivez ses résumés d'une ligne dans `readme/summaries.json`, lancez `python3 scripts/build-catalog.py` et ouvrez une pull request.

## Remerciements

Chaque mod appartient à son auteur et garde sa propre licence ; ce dépôt ne fait que les répertorier. Beaucoup ont été trouvés grâce à [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods). Les auteurs qui souhaitent modifier ou retirer une fiche peuvent ouvrir une issue.

Projet non officiel ; ce n'est pas un produit Anthropic.
