from traceback import print_tb
from hardware.field import *
from hardware.field.nodes import *
import time
import tcp
from threading import Thread

centrifuge = Centriguge()
crusher = Crusher()
tank = Tank()

plc = PLC()

def data_send(self):
    while True:
        for value in self.send_sensors_values():
            tcp.write(self.client, value)
            time.sleep(0.7)
        time.sleep(5)

def message_handler(self):
     while True:
        try:
            msg = self.client.recv(1024).decode('utf-8')
            if msg:
                if msg.start_with("[CONTROL]"):
                    msg = msg[10:].split(":")
                    self.write_to_analog(msg[0], int(msg[1]))
        except Exception as e:
            print(e)
            self.client.close()
            break

def init(self):
    self.client = tcp.start_client(message_handler)
    #Thread(target=data_send, args=(self,)).start()

def tick(self):
    if self.get("AI1") < 10:
        self.write_to_analog("AO1", 20)
    centrifuge.tick()
    crusher.tick()
    tank.tick()
    time.sleep(0.2)



oil_level_sensor = Sensor(SensorType.OIL_LEVEL, "Siemens MF1570","ANALOG", lambda x: crusher.oil_level)
centrifuge_rotation_speed = Sensor(SensorType.ROTATION_SPEED,"IFM Electronic MX5000 Centrifuge", "ANALOG", lambda x: centrifuge.rotation_speed)
rotor_rotation_speed = Sensor(SensorType.ROTATION_SPEED,"IFM Electronic MX5000 Tank", "ANALOG", lambda x: tank.rotation_speed)
centrifuge_temperature = Sensor(SensorType.TEMPERATURE,"IFM Electronic TA2417 Centrifuge", "ANALOG", lambda x: centrifuge.temperature)
tank_temperature = Sensor(SensorType.TEMPERATURE,"IFM Electronic TA2417 Tank", "ANALOG", lambda x: tank.temperature)
tank_pressure = Sensor(SensorType.TEMPERATURE,"APZ 3420s", "ANALOG", lambda x: (tank.liquid_level * 9.8 * 1030))

crusher_drive = Executor("Привод дробилки", crusher.switch)
oil_injector = Executor("Смазочное устройство", crusher.add_oil)
centrifuge_drive = Executor("Привод центрифуги", centrifuge.switch)
centrifuge_heater = Executor("Нагреватель центрифуги", centrifuge.apply_heat)
tank_drive = Executor("Привод лопастей сироповарки", tank.apply_rotation_power)
tank_heater = Executor("Нагреватель сироповарки", tank.apply_heat)
tank_pump = Executor("Насос", tank.pump_out)


plc.add_sensor("AI1", oil_level_sensor)
plc.add_sensor("AI2", centrifuge_rotation_speed)
plc.add_sensor("AI3", rotor_rotation_speed)
plc.add_sensor("AI4", centrifuge_temperature)
plc.add_sensor("AI5", tank_temperature)
plc.add_sensor("AI6", tank_pressure)

plc.add_executor("AO1", oil_injector)

plc.set_init_func(init)
plc.set_tick_func(tick)
plc.start()


while True:
    print(crusher.oil_level)
    time.sleep(0.2)

