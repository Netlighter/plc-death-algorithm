from traceback import print_tb
from hardware.field import *
from hardware.field.nodes import *
import time
import tcp
from threading import Thread
import os

plc = PLC()


def data_send(self):
    while True:
        for value in self.send_sensors_values():
            tcp.write(self.client, value)
            print(value)
        time.sleep(1)


def message_handler(self):
    while True:
        try:
            msg = self.client.recv(1024).decode('utf-8')
            
            if msg:
                print(msg)
                if msg.startswith("[CONTROL]"):
                    msg = msg[10:].split(":")
                    self.write_to_analog(msg[0], int(msg[1]))
        except Exception as e:
            print(e)
            self.client.close()
            break


bunkers = []
level_sensors = []
for i in range(2):
    bunkers.append(AASBunker(i, 200))
    level_sensors.append(Sensor(SensorType.ALUMINA_LEVEL, f"Сенсор {i}", "ANALOG", lambda t, b=bunkers[i]: b.level, id=i+1))
    plc.add_sensor(f"A{i}", level_sensors[i])

def init(self):
    print(plc.inputs)
    pass
    self.client, recv_thread = tcp.start_client(message_handler, args=(self,))
    recv_thread.start()
    Thread(target=data_send, args=(self,)).start()


def tick(self):
    for bunker in bunkers:
        bunker.tick()
    
    time.sleep(0.2)


plc.set_init_func(init)
plc.set_tick_func(tick)
plc.start()
