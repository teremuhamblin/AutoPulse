###### README.md >> markdown 
# AutoPulse
>Moteur d'automatisme modulaire
- Control

---

[![Dependency Graph](https://github.com/teremuhamblin/AutoPulse/actions/workflows/dependabot/update-graph/badge.svg)](https://github.com/teremuhamblin/AutoPulse/actions/workflows/dependabot/update-graph)

---

### Fonction modulaire :
- State machine process
- Séquences YAML
- I/O virtuels + Modbus/TCP (stub)
- API REST (FastAPI)
- Web UI minimal

### Structure du projet

---

[![pages-build-deployment](https://github.com/teremuhamblin/AutoPulse/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/teremuhamblin/AutoPulse/actions/workflows/pages/pages-build-deployment)

---

```text
AutoPulse
 ├─ .github
 │   ├─ workflows
 ├─ README.md
 ├─ pyproject.toml
 ├─ ROADMAP.md 
 ├─ CHANGELOG.md 
 ├─ autopulse/
 │   ├─ README.md 
 │   ├─ __init__.py
 │   ├─ state_machine.py
 │   ├─ sequence_engine.py
 │   ├─ io.py
 │   ├─ api.py
 │   └─ sequences.yaml
 ├─ webui/
 │   ├─ README.md 
 │   ├─ app.js
 │   └─ index.html
 ├─ docker/
 │   ├─ README.md 
 │   ├─ Dockerfile
```

### Dev
```pip
pip install -e
uvicorn autopulse.api.main:app --reload
```

### UI 
- Disponible dans :
```md
webui/index.html
```



