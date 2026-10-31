# Personal shopper

Ce dépôt est l'outil d'aide à l'achat de l'utilisatrice. Chaque besoin d'achat = un dossier dans `achats/`.

## Comment travailler
- Pour tout besoin d'achat, suis le skill `personal-shopper` (`.claude/skills/personal-shopper/SKILL.md`).
- Lis d'abord `profil.md` et `achats/README.md`.
- Nouveau besoin : crée `achats/AAAA-MM-<slug>/` à partir de `modeles/`.
- Réponds en français, tutoiement, résultat d'abord, formats lisibles sur téléphone.
- Enregistre (commit + push) à chaque étape franchie, pour pouvoir reprendre dans une autre session.

## Comparateur en ligne
- Chaque projet d'achat a aussi un espace dans le **Carnet d'achats** : https://claude.ai/artifact/VuTVNiFG2FryKBy8qepncQ (voir `comparateur/README.md`).
- Quand une reco est prête, ajoute ou mets à jour le projet dans la base de la page (ArtifactData), sans écraser le champ `weights`.

## Fichiers
- `profil.md` : goûts et contraintes durables. À enrichir après chaque achat.
- `achats/README.md` : journal de tous les achats.
- `modeles/` : modèles de brief et de reco.
