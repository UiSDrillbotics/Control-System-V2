class Rotation:

    def __init__(self):
        self.calibrated = False
        self._rpm = 0
        self._torque = 0


    @property
    def rpm(self):
        return self.rpm

    @rpm.setter
    def rpm(self, rotation):
        self.rpm = rotation

    @property
    def torque(self):
        return self.torque

    @torque.setter
    def torque(self, torque):
        self.torque = torque

    

    