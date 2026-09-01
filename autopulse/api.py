from fastapi import FastAPI
from .io import IO
from .state_machine import Machine
from .sequence_engine import SequenceEngine

app = FastAPI()

io = IO()
machine = Machine()
seq = SequenceEngine()

@app.get("/status")
def status():
    return {
        "state": machine.state,
        "inputs": io.get_inputs(),
        "outputs": io.outputs
    }

@app.post("/io/{name}/{value}")
def set_io(name: str, value: bool):
    io.set_input(name, value)
    machine.update(io.get_inputs())
    return {"ok": True}

@app.post("/sequence/{name}")
def start_sequence(name: str):
    seq.start(name)
    return {"started": name}

@app.get("/tick")
def tick():
    out = seq.tick()
    io.set_outputs(out)
    return out
