# Structure 
```text
AutoPulse/
 ├─ README.md
 ├─ pyproject.toml
 ├─ autopulse/
 │   ├─ __init__.py
 │   ├─ core/
 │   │   ├─ state_machine.py
 │   │   ├─ sequence_engine.py
 │   │   ├─ scheduler.py
 │   │   └─ alarms.py
 │   ├─ io/
 │   │   ├─ base_io.py
 │   │   ├─ virtual_io.py
 │   │   ├─ modbus_tcp.py
 │   │   └─ mapping.yaml
 │   ├─ api/
 │   │   ├─ __init__.py
 │   │   ├─ main.py
 │   │   ├─ routes_status.py
 │   │   ├─ routes_io.py
 │   │   └─ routes_sequences.py
 │   ├─ supervisor/
 │   │   ├─ dashboard.py
 │   │   ├─ trends.py
 │   │   └─ events_log.py
 │   └─ config/
 │       ├─ settings.yaml
 │       ├─ sequences/
 │       │   ├─ example_startup.yaml
 │       │   └─ example_batch.yaml
 │       └─ alarms.yaml
 ├─ webui/
 │   ├─ index.html
 │   ├─ css/
 │   │   └─ tailwind.css
 │   └─ js/
 │       └─ app.js
 ├─ tests/
 │   ├─ test_state_machine.py
 │   ├─ test_sequences.py
 │   └─ test_virtual_io.py
 └─ docker/
     ├─ Dockerfile
     └─ compose.yaml
```
