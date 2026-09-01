import yaml

class SequenceEngine:
    def __init__(self, path="autopulse/sequences.yaml"):
        self.data = yaml.safe_load(open(path))
        self.active = None
        self.step = 0

    def start(self, name):
        self.active = self.data[name]
        self.step = 0

    def tick(self):
        if not self.active:
            return {}
        outputs = self.active[self.step].get("outputs", {})
        self.step += 1
        if self.step >= len(self.active):
            self.active = None
        return outputs
