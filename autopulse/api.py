@app.post("/start")
def start_engine():
    engine.start()
    return {"status": "started"}

@app.post("/stop")
def stop_engine():
    engine.stop()
    return {"status": "stopped"}

@app.post("/tick")
def tick():
    return engine.tick()
