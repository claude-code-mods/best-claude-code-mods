# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**Choisis à la main, validés, épinglés. Un seul ajout, 43 mods.**

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

### Tableaux de bord et usage

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>par hamzafer</sub> | Une ligne sous la barre d'état : minutes de cache encore chaud, et tokens que le prochain message remettra en cache | fichiers, lance des commandes |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>par hamzafer</sub> | La fenêtre de contexte en barre empilée, une couleur par catégorie, avec tokens et point de compaction (/context-bar) | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>par hamzafer</sub> | Solde estimé de l'API OpenAI, dépenses du jour et où part l'argent (/openai-balance) | réseau, lance des commandes |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>par hamzafer</sub> | L'usage du contexte en bulletin météo, avec le compte à rebours du cache de prompt | fichiers, lance des commandes |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>par hamzafer</sub> | Usage 5 heures et 7 jours en petites barres, avec compte à rebours de réinitialisation et coût de la session | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>par JetsonChan</sub> | Limites 5 heures et 7 jours, contexte et taux de cache au-dessus du prompt, en terminal comme dans l'app de bureau | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>par kongyo2</sub> | Le contexte sur une ligne, dessiné comme les jauges de Claude Code, avec ce qu'il reste avant la compaction automatique | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>par scasella</sub> | Tableau de bord des agents : état du modèle, chaque décision de permission, cartes et couloirs des sous-agents, reçu du tour et journal de session | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>par tomstagl</sub> | Tableau de bord en direct façon btop : contexte, tokens, coût, taux de cache, limites et latence par outil (/cctop) | fichiers, lance des commandes |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>par xuanji86</sub> | Carte d'état flottante au-dessus du prompt : modèle, effort, contexte, limites 5 h et hebdo, coût, branche et CI | fichiers, lance des commandes |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>par zycck</sub> | Barres de progression du plan au-dessus du prompt : étapes, remplissage pixel et sons discrets pour décision, erreur et fin | fichiers, lance des commandes |

### Agents et sous-agents

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>par Charlie0113-T</sub> | /flow ouvre à côté de la conversation un arbre en direct des sous-agents et coéquipiers | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>par hamzafer</sub> | Une ligne par sous-agent actif : durée, nombre d'outils et activité (/radar les montre tous) | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>par hamzafer</sub> | Montre qui tient le navigateur Playwright ; les sous-agents attendent leur tour, /browser clean ferme les restes | lance des commandes |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>par hamzafer</sub> | /mission ouvre une carte en direct de l'agent principal, des sous-agents et de chaque appel d'outil, plus une carte des fichiers | fichiers, appelle un modèle, lance des commandes |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>par hamzafer</sub> | Une ligne en direct par revue de code en cours (Codex ou sous-agent), et une notification des constats à la fin | lance des commandes |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>par hamzafer</sub> | Choisit le modèle des sous-agents qui n'en nomment pas (OpenAI Decisions API ou Jev) ; /route montre choix et coûts | réseau |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>par xuanji86</sub> | Panneau latéral des sous-agents : ce que fait chacun, ses tokens, et sa conversation en un clic | — |

### Productivité et contexte

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>par hamzafer</sub> | Ce qui vous attend sur une ligne : prochaine réunion, PR, tickets Linear et messages Slack (via MCP connecté) | MCP, lance des commandes |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>par hamzafer</sub> | Après chaque tour, 2 ou 3 prompts suivants probables ; tapez 1, 2 ou 3 dans un prompt vide pour en reprendre un | appelle un modèle |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>par hamzafer</sub> | Nomme les sessions sans titre ; /park note où vous en étiez et le montre à la reprise | appelle un modèle, lance des commandes |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>par hamzafer</sub> | Résumé en direct au-dessus du prompt : objectif, en cours, ce qui vous attend, prochaine étape (/where détaille) | appelle un modèle |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>par JayDoubleu</sub> | Discussion annexe en lecture seule : /aside pour interroger la session sans rien écrire dans le fil principal | appelle un modèle |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>par lossless-claude</sub> | Gestion du contexte sans perte : résumés en DAG qui gardent chaque message accessible | fichiers, réseau, appelle un modèle, lance des commandes |

### Rendu et aperçus

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>par briangtn</sub> | Markdown façon GitHub dans la conversation : alertes, listes de tâches, texte barré et diagrammes Mermaid | lance des commandes |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>par hamzafer</sub> | Les fichiers Markdown modifiés par Claude rendus comme sur GitHub dans un panneau, avant et après côte à côte (/md) | fichiers, lance des commandes |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>par hamzafer</sub> | Rejoue les modifications de fichiers du dernier tour, un diff à la fois | fichiers |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>par hellosverre</sub> | Des thèmes pour la conversation : lignes d'outils, marges des réponses et textes du spinner ; /skin les change à chaud | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>par xuanji86</sub> | Cliquez sur un chemin .md de la conversation pour le lire rendu à côté, images comprises, et désignez un bloc à faire modifier par Claude | fichiers, lance des commandes |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>par zenbu-labs</sub> | Un navigateur à côté de la conversation : aperçu de sites web et de HTML local, que l'agent peut aussi piloter | fichiers, réseau, lance des commandes |

### Sécurité et garde-fous

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>par hamzafer</sub> | Retient les commandes Bash risquées et montre ce qu'elles changeraient avant votre accord | lance des commandes |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>par hamzafer</sub> | Bloque `gh pr merge` tant que la CI n'est pas verte et qu'une revue Codex n'a pas tourné | fichiers, lance des commandes |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>par hamzafer</sub> | Règles d'écriture et de git : remplace les tirets cadratins et demande avant un amend, un push non formaté ou des données personnelles | fichiers, lance des commandes |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>par ray-amjad</sub> | Remplace secrets, e-mails et IP par des marqueurs stables avant la conversation, et les rétablit dans les appels d'outils | — |

### Git, PR et déploiements

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>par ray-amjad</sub> | La file de déploiements Vercel du projet lié, épinglée sous le prompt, avec phase et durée | fichiers, lance des commandes |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>par sezaakgun</sub> | État de fusion, revues et checks requis des PR GitHub suivies, avec alerte quand ils changent | fichiers, lance des commandes |

### Pendant l'attente

| Mod | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>par darrell-tw</sub> | Liste de suivi des actions taïwanaises et américaines selon l'heure de marché, avec mode plus-values | fichiers, réseau, lance des commandes |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>par halluton</sub> | Exercices de respiration guidés au-dessus du prompt pendant que Claude travaille ; le spinner compte avec vous | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>par hamzafer</sub> | Ce que joue Spotify sur une ligne : titre, progression et paroles en cours, avec boutons (macOS seulement) | réseau, lance des commandes |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>par hamzafer</sub> | La prière en cours, la suivante et le temps restant, calculés sur votre machine sans rien envoyer | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>par hamzafer</sub> | Des YouTube Shorts dans un panneau du terminal : lecture pendant que Claude travaille, pause à la fin | fichiers, réseau, lance des commandes |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>par hamzafer</sub> | Snake dans un panneau pendant que Claude travaille ; rien ne s'ouvre avant /snake | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>par sezaakgun</sub> | Neuf jeux au-dessus du prompt (snake, blocs, 2048…) et un compagnon qui grandit avec les tests et commits | — |

## Proposer un mod

Ouvrez une issue avec le lien vers le dépôt du mod. Pour l'ajouter vous-même, ajoutez une entrée dans `community.json` (dépôt, dossier, commit relu, catégorie, licence), écrivez ses résumés d'une ligne dans `readme/summaries.json`, lancez `python3 scripts/build-catalog.py` et ouvrez une pull request.

## Remerciements

Chaque mod appartient à son auteur et garde sa propre licence ; ce dépôt ne fait que les répertorier. Beaucoup ont été trouvés grâce à [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods). Les auteurs qui souhaitent modifier ou retirer une fiche peuvent ouvrir une issue.

Projet non officiel ; ce n'est pas un produit Anthropic.
