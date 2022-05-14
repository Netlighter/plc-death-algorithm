from enum import Enum

class SensorType(Enum):
    NONE = 0
    TEMPERATURE = 1
    LEVEL = 2
    ROTATION_SPEED = 3
    HUMIDITY = 4


class Sensor():
    def __init__(self, sensor_type, name, con_type, output_func):
        self.name = name
        self.type: SensorType = sensor_type
        self.connection_type = con_type
        self.evaluate = output_func
