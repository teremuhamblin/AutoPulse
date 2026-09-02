```text
AutoPulse/Docs/README.md

Il couvre :

- Architecture du moteur  
- API REST  
- Modules internes  
- WebUI  
- Séquences  
- Scheduler / Alarmes / Timeline  
- Roadmap documentaire
```

---

###### 📘 README.md >> markdown 
- Dossier docs/
- AutoPulse v1.2.0

📘 Documentation Officielle
Dossier docs/ — Version 1.2.0  
Auteur : Major HAMBLIN Teremu
Projet : AutoPulse
- Moteur d’automatisme modulaire

---

🧭 1. Présentation du dossier docs/

Ce dossier contient toute la documentation technique du projet AutoPulse :

- Architecture interne du moteur
- API REST (FastAPI)
- Modules internes (Scheduler, Alarmes, Timeline, EventBus)
- Gestion des séquences YAML
- Structure du projet
- Notes de développement
- Roadmap technique

Chaque fichier est conçu pour être clair, militaire, et immédiatement exploitable.

---

🧩 2. Structure du dossier

```text
docs/
 ├─ architecture.md
 ├─ api.md
 ├─ modules.md
 ├─ sequences.md
 ├─ webui.md
 └─ notes.md
```

---

🏗️ 3. Architecture du moteur (résumé)

AutoPulse repose sur une architecture modulaire :

- engine.py — moteur central
- state_machine.py — machine d’état
- sequence_engine.py — séquences YAML
- events.py — EventBus interne
- scheduler.py — cadence automatique
- alarms.py — gestion des alarmes
- timeline.py — historique des ticks
- api.py — API REST FastAPI

L’objectif est de fournir un moteur léger, extensible, et stable.

---

🔌 4. API REST (résumé)

Endpoints principaux :

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| GET | /status | État complet du moteur |
| POST | /start | Démarre le moteur |
| POST | /stop | Arrête le moteur |
| POST | /tick | Avance d’un pas |
| POST | /sequence/{name} | Exécute une séquence YAML |

Réponses uniformisées en JSON.

---

⚙️ 5. Modules internes (résumé)

✔ Scheduler
- Intervalle configurable  
- Prochain tick  
- Mode RUN/HOLD  

✔ Alarmes
- Trigger / Reset  
- Historique des alarmes  
- Intégration EventBus  

✔ Timeline
- Historique des ticks  
- Limite configurable  
- Intégration WebUI  

✔ EventBus
- Journalisation interne  
- Hooks modulaires  
- Intégration moteur + API  

---

📜 6. Séquences YAML

Les séquences sont définies dans :

`
autopulse/sequences.yaml
`

Exemple :

`yaml
startup:
  - init
  - check_io
  - ready
`

Le SequenceEngine valide et exécute chaque étape.

---

🖥️ 7. WebUI (résumé)

La WebUI v1.2.0 inclut :

- Panneau État moteur  
- Panneau Scheduler  
- Panneau Alarmes  
- Timeline  
- I/O  
- Événements  
- JSON brut  
- Boutons tactiques (Start / Stop / Tick / Sequence)

Fichiers :

`
webui/index.html
webui/app.js
`

---

🚀 8. Roadmap documentaire

v1.3.0
- Documentation WebSockets
- Documentation HUD Ghost Recon
- Documentation modules dynamiques

v1.4.0
- Documentation mode Simulation
- Documentation plugins externes

v2.0.0
- Documentation architecture Next‑Gen
- Documentation production industrielle

---

📝 9. Notes du développeur

AutoPulse est conçu pour être :

- simple à comprendre  
- rapide à déployer  
- facile à étendre  
- stable en production  
- militaire dans sa structure  

Ce dossier docs/ est la base de la documentation officielle du projet.

`

---

🟩
