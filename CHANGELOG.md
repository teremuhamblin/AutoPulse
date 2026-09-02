# 📗 AutoPulse — CHANGELOG Officiel

---

## 🟩 v1.2.0 — Scheduler + Alarmes + Timeline (02/09/2026)
### Nouveautés
- Ajout du module `scheduler.py`
- Ajout du module `alarms.py`
- Ajout du module `timeline.py`
- Mise à jour du moteur `engine.py`
- Ajout des champs `scheduler`, `alarms`, `timeline` dans `/status`
- WebUI v1.2.0 (panneaux + actions tactiques)
- Nouveau fichier `app.js` (JS séparé)
- Architecture modulaire complète

### Améliorations
- EventBus optimisé
- SéquenceEngine stabilisé
- API REST uniformisée

---

## 🟩 v1.1.0 — Stabilization Upgrade (01/09/2026)
### Nouveautés
- Ajout du module `events.py`
- Hooks internes : `on_state_change`, `on_sequence_step`, `on_io_update`
- WebUI améliorée (Events + I/O)
- Documentation architecture + API

### Améliorations
- SéquenceEngine : validation renforcée
- API REST : cohérence JSON
- Structure du projet stabilisée

---

## 🟩 v1.0.0 — Foundation Build (31/08/2026)
### Nouveautés
- Moteur AutoPulseEngine minimal
- StateMachine basique
- SequenceEngine YAML
- API REST FastAPI minimale
- WebUI simple (status JSON)
- Structure initiale du projet

---

# 📝 Format du versioning
AutoPulse utilise le versioning **SemVer** :
- MAJOR : rupture / architecture
- MINOR : nouvelles fonctionnalités
- PATCH : corrections / stabilité

---

# 🔰 Notes du développeur
AutoPulse suit une progression militaire :
- v1.x → construction du moteur
- v2.x → automatisme avancé
- v3.x → production industrielle
