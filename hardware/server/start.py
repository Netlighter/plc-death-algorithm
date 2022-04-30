#from .field import *
from server import *


server = start_server(7777,1)
wait_connection(server)



# plc = PLC()
# def tick(self):
#     print(self.get("A1")/self.get("A2"))


# plc = PLC()

# temperature_sensor = Sensor(SensorType.TEMPERATURE, "ANALOG", lambda t: t/1000)
# humidity_sensor = Sensor(SensorType.ROTATION_SPEED, "ANALOG", lambda t: t/1000+15)
# plc.add_sensor("A1", temperature_sensor)
# plc.add_sensor("A2", humidity_sensor)

# plc.set_tick_func(tick)
#plc.start()
