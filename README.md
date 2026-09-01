###### README.md >> markdown 
# AutoPulse
>Moteur d'automatisme modulaire
- Control

### Fonction modulaire :
- State machine process
- Séquences YAML
- I/O virtuels + Modbus/TCP (stub)
- API REST (FastAPI)
- Web UI minimal

### Structure du projet
```text
AutoPulse
 ├─ README.md
 ├─ pyproject.toml
 ├─ autopulse/
 │   ├─ __init__.py
 │   ├─ state_machine.py
 │   ├─ sequence_engine.py
 │   ├─ io.py
 │   ├─ api.py
 │   └─ sequences.yaml
 ├─ webui/
 │   └─ index.html
 └─ docker/
     └─ Dockerfile
```

### Dev
```bash
pip install -e .
uvicorn autopulse.api.main:app --reload
```
