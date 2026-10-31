# Carnet d'achats (comparateur en ligne)

Page privée : https://claude.ai/artifact/VuTVNiFG2FryKBy8qepncQ

- `carnet.html` : la page (publiée avec l'outil Artifact, capacité `db`).
- `data/` : les données de chaque projet, source de vérité versionnée.
  - `<slug>.project.json` → document `projects/<slug>` (besoin, critères pondérés, verdict, écartés, notes).
  - `<slug>.<id>.json` → document `projects/<slug>/products/<id>` (prix, où acheter, note 0–10 par critère avec la valeur mesurée et les sources).
- `build_<slug>.py` : génère les JSON d'un projet.

Mise à jour : modifier le script ou le JSON, relancer, puis écrire dans la base avec `ArtifactData` (batch, `if_version` obligatoire sur les documents existants). Les pondérations réglées par l'utilisatrice sont stockées dans le champ `weights` du document projet : ne pas l'écraser (utiliser `update` plutôt que `set` sur un projet existant).

Le critère dont `auto` vaut `price` est calculé par la page : 10/10 au prix `best`, 0/10 au prix `worst`.
