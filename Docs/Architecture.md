# 📘 DOCUMENTATION 1 :
- Architecture & Concepts
   - AutoPulse
   - Documentation Technique

### Architecture
- Concepts, Automatisme Modulaire

AutoPulse-Control est un moteur d’automatisme minimaliste conçu pour :
- piloter des états,
- exécuter des séquences,
- gérer des entrées/sorties virtuelles,
- exposer une API REST simple,
- fonctionner dans un environnement léger (Termux, Docker, Linux embarqué).

---

### 1. Architecture générale
```text
autopulse/
 ├─ state_machine.py      → Machine d’état
 ├─ sequence_engine.py    → Moteur de séquences
 ├─ io.py                 → I/O virtuels
 ├─ api.py                → API FastAPI
 └─ sequences.yaml        → Séquences d’automatisme
```
>AutoPulse repose sur trois blocs principaux :

#### 1.1 Machine d’état
La machine d’état gère les transitions :
- STOPPED → RUNNING
- RUNNING → STOPPED

Elle lit les entrées virtuelles (start, stop) et met à jour l’état.

#### 1.2 Moteur de séquences
Le moteur lit sequences.yaml et exécute les étapes une par une.

Chaque étape contient :
```yaml
- outputs:
    valve_open: true
```

Le moteur renvoie les sorties à appliquer.

#### 1.3 I/O virtuels
Les I/O sont stockées en mémoire :
- inputs : commandes opérateur
- outputs : actionneurs simulés

#### 1.4 API REST
Expose :
- /status → état + I/O
- /io/{name}/{value} → modifier une entrée
- /sequence/{name} → lancer une séquence
- /tick → avancer d’un pas dans la séquence

---

### 2. Fonctionnement interne
#### 2.1 Cycle d’automatisme
1. L’opérateur envoie une commande via l’API.  
2. La machine d’état se met à jour.  
3. Si RUNNING → une séquence peut être lancée.  
4. Le moteur de séquence renvoie les sorties.  
5. Les sorties sont appliquées dans IO.outputs.  

---

### 3. Séquences YAML
Exemple :
```yaml
startup:
  - outputs: { valve_open: true }
  - outputs: { pump_run: true }
```

Chaque étape est exécutée dans l’ordre.

---

### 4. Avantages du moteur
- Ultra léger  
- Aucun framework lourd  
- API REST intégrée  
- Séquences lisibles  
- Compatible Termux / Docker / Linux embarqué  
- Parfait pour prototypage d’automatisme  

---

### 5. Limites actuelles
- Pas de gestion du temps par étape  
- Pas de Modbus natif  
- Pas de supervision avancée  
- Pas de gestion d’alarmes  

---

### 6. Extensions possibles
- Ajout d’un scheduler temps réel  
- Ajout d’un driver Modbus/TCP  
- Ajout d’un dashboard web avancé  
- Ajout d’un système d’alarmes  
- Ajout d’un moteur de scripts Python  

---

### 7. Licence
`
Projet open-source, libre d’utilisation.
`

---

# 📗 DOCUMENTATION 2 :
- API & Intégration (docs_api.md)
### AutoPulse
- Documentation API & Intégration

Cette documentation décrit l’API REST, les endpoints, les formats de données et les méthodes d’intégration.

---

### 1. API REST
Base URL :
```md
http://localhost:8000
```

---

### 2. Endpoints
#### 2.1 GET /status
Retourne l’état du moteur.

Exemple
```json
{
  "state": "RUNNING",
  "inputs": { "start": true, "stop": false },
  "outputs": { "valve_open": true }
}
```

---

#### 2.2 POST /io/{name}/{value}
Modifie une entrée.

Exemple
```md
POST /io/start/true
```

Effet :
- met inputs["start"] = true
- met à jour la machine d’état

---

#### 2.3 POST /sequence/{name}
Lance une séquence définie dans sequences.yaml.

Exemple
```md
POST /sequence/startup
```

---

#### 2.4 GET /tick
Avance d’un pas dans la séquence active.

Exemple
```json
{
  "valve_open": true
}
```

---

### 3. Intégration dans un système externe
#### 3.1 Exemple en Python

```python
import requests

requests.post("http://localhost:8000/io/start/true")
requests.post("http://localhost:8000/sequence/startup")

while True:
    out = requests.get("http://localhost:8000/tick").json()
    print(out)
```

---

#### 3.2 Exemple en JavaScript
```js
await fetch("/io/start/true", { method: "POST" });
await fetch("/sequence/startup", { method: "POST" });

setInterval(async () => {
  const tick = await (await fetch("/tick")).json();
  console.log(tick);
}, 1000);
```

---

### 4. Intégration Docker
#### 4.1 Build
```bash
docker build -t autopulse .
```

### 4.2 Run
```bash
docker run -p 8000:8000 autopulse
```

---

### 5. Intégration Termux
AutoPulse fonctionne parfaitement dans Termux :
```bash
pkg install python
pip install fastapi uvicorn pyyaml
uvicorn autopulse.api:app --reload
```

---

### 6. Sécurité API
- Pas d’authentification (version minimaliste)
- À utiliser derrière un reverse proxy si exposé
- Ajouter un token si nécessaire

---

### 7. Bonnes pratiques
- Toujours appeler /tick dans une boucle
- Ne jamais modifier sequences.yaml en cours d’exécution
- Utiliser des noms simples pour les I/O

---

### 8. Roadmap API
- Ajout d’un endpoint /alarms
- Ajout d’un endpoint /scheduler
- Ajout d’un endpoint /modbus
- Ajout d’un endpoint /sequence/stop

---

### 9. Licence

Libre d’utilisation.
`

---
