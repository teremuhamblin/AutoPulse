class IO:
    def __init__(self):
        self.inputs = {"start": False, "stop": False}
        self.outputs = {}

    def set_input(self, name, value):
        self.inputs[name] = value

    def get_inputs(self):
        return self.inputs

    def set_outputs(self, outputs):
        self.outputs.update(outputs)
