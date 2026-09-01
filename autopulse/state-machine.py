class Machine:
    def __init__(self):
        self.state = "STOPPED"

    def update(self, io):
        if self.state == "STOPPED" and io.get("start"):
            self.state = "RUNNING"
        elif self.state == "RUNNING" and io.get("stop"):
            self.state = "STOPPED"
