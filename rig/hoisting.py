class Hoisting:

    def __init__(self):
        self.calibrated = False
        self.wob = 0
        self.brake = Brake()
        self.actuator = Actuator()
        self.stepper1 = Stepper()
        self.stepper2 = Stepper()
        self.stepper3 = Stepper()
        self.load_cell = LoadCell()
        
    
    def calibrate(self):
        self.brake.open()

        # TODO Implement calibration procedure

        self.calibrated = True

    def move(self):
        pass


    @property
    def wob(self):
        return self.wob

    @wob.setter
    def wob(self, weight):
        self.wob = weight

    def telemetry(self):
        pass


class Actuator(Hoisting):

    def __init__(self):
        pass


class Stepper(Hoisting):

    def __init__(self):
        self.counter = 0

    


class Brake(Hoisting):

    def __init__(self):
        self.brake = True

    def __bool__(self):
        return self.brake

    def open(self):
        # TODO Open the brake (will do nothing if already open)

        self.brake = False
    
    def close(self):
        # TODO Close the brake (will do nothing if already closed)

        self.brake = True


class LoadCell(Hoisting):

    def __init__(self):
        pass




    

    

    

    

