from sqlalchemy import true


class Centriguge():
    def __init__(self):
        self.rotation_speed = 0
        self.temperature = 0
        self.enabled = False

    def apply_rotation_power(self, power):
        self.rotation_speed += power

    def apply_heat(self, power):
        self.temperature += power

    def switch(self, value):
        self.enabled = value

    def tick(self):
        self.rotation_speed -= 1
        self.rotation_speed = max(0, self.rotation_speed)
        self.temperature -= 1
        self.temperature = max(0, self.temperature)


class Crusher():
    def __init__(self):
        self.oil_level = 0
        self.enabled = False

    def add_oil(self, oil):
        self.oil_level += oil

    def switch(self, value):
        self.enabled = value

    def tick(self):
        self.oil_level -= 0.5
        self.oil_level = max(0, self.oil_level)



class Tank():
    def __init__(self):
        self.temperature = 0
        self.liquid_level = 0
        self.rotation_speed = 0
        self.enabled = False

    def apply_rotation_power(self, power):
        self.rotation_speed += power

    def add_liquid(self, liquid):
        self.liquid_level += liquid

    def apply_heat(self, power):
        self.temperature += power

    def switch(self):
        self.enabled = not self.enabled

    def pump_out(self, value):
        self.liquid_level -= value

    def tick(self):
        self.rotation_speed -= 1
        self.rotation_speed = max(0, self.rotation_speed)
        self.temperature -= 1
        self.temperature = max(0, self.temperature)
        self.liquid_level -= 1
        self.liquid_level = max(0, self.liquid_level)
