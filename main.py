from typing import List, Tuple, Dict, Set
from enum import Enum
from random import randint

class SensorType(Enum):
    NONE = 0
    TEMPERATURE = 1
    LEVEL = 2
    ROTATION_SPEED = 3


class PLC:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        self.tick = 0
    
    def add_sensor(self, port,sensor):
        self.inputs[port] = sensor

    def add_executor(self, port, executor):
        self.outputs[port] = executor

    def get(self, port):
        return self.inputs[port].evaluate(self.tick)

class Sensor():
    def __init__(self, sensor_type, con_type, output_func):
        self.type: SensorType = sensor_type
        self.connection_type = con_type
        self.evaluate = output_func

class Executor():
    def __init__(self):
        pass



plc = PLC()

temperature_sensor  = Sensor(SensorType.TEMPERATURE, "ANALOG", lambda t: randint(1,255))

plc.add_sensor("A1", temperature_sensor)

