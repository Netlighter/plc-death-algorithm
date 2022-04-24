from enum import Enum

class SensorType(Enum):
    NONE = 0
    TEMPERATURE = 1
    LEVEL = 2
    ROTATION_SPEED = 3


class Sensor():
    def __init__(self, sensor_type, con_type, output_func):
        self.type: SensorType = sensor_type
        self.connection_type = con_type
        self.evaluate = output_func
