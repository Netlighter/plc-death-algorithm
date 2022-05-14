from traceback import print_tb
from hardware.field import *
from tcp.client import start_client, write
import time

plc = PLC()
def init(self):
    self.client = start_client()

def tick(self):
    write(self.client, f'[SEND SQL] [SENSOR] {self.get_sensor_info("A1").name}:20')
    time.sleep(1)

temperature_sensor = Sensor(SensorType.TEMPERATURE, "Датчик температуры","ANALOG", lambda t: t/1000)
humidity_sensor = Sensor(SensorType.ROTATION_SPEED,"Датчик влажности", "ANALOG", lambda t: t/1000+15)
plc.add_sensor("A1", temperature_sensor)
plc.add_sensor("A2", humidity_sensor)

plc.set_init_func(init)
plc.set_tick_func(tick)
plc.start()
