###### README.md >> markdown 
# AutoPulse
>Moteur d'automatisme modulaire
- Control

Moteur d’automatisme modulaire :
- State machine process
- Séquences YAML
- I/O virtuels + Modbus/TCP (stub)
- API REST (FastAPI)
- Web UI minimal

### Dev
```bash
pip install -e .
uvicorn autopulse.api.main:app --reload
```
