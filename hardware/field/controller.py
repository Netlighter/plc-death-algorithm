class PLC:
    def __init__(self):
        self.tick = 0
        self.inputs = {}
        self.outputs = {}
        self.init_prg = None
        self.tick_prg = None

    def add_sensor(self, port, sensor):
        self.inputs[port] = sensor

    def add_executor(self, port, executor):
        self.outputs[port] = executor
        
    def get(self, port):
        if not self.inputs.get(port):
            raise Exception(f'[CONTROLLER ERROR] Port {port} is not assigned.')
        return self.inputs[port].evaluate(self.tick)

    def set_init_func(self, func):
        self.init_prg = func

    def set_tick_func(self, func):
        self.tick_prg = func

    def start(self):
        if self.init_prg:
            self.init_prg(self)
        if not self.tick_prg:
            raise Exception('[CONTROLLER ERROR] Update function is not set.')
        while True:
            self.tick_prg(self)
            self.tick+=1
