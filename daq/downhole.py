class Downhole:

    def __init__(self):
        self.accelerometer = Accelerometer()
        self.magnetometer = Magnetometer()
        self.gyroscope = Gyroscope()
        print("Downhole initialized")

    def new_measurement(self):
        # Get raw sensor data and store in the object itself



        # Dummy values
        
        pass

    def math_calculations(self):
        pass
        

class Accelerometer(Downhole):
    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0
        self.z_axis = 0

    @property
    def x_axis(self):
        return self.x_axis

    @x_axis.setter
    def x_axis(self, x):
        self.x_axis = x

    @property
    def y_axis(self):
        return self.y_axis

    @y_axis.setter
    def y_axis(self, y):
        self.y_axis = y

    @property
    def z_axis(self):
        return self.z_axis

    @z_axis.setter
    def z_axis(self, z):
        self.z_axis = z





class Magnetometer(Downhole):
    def __init__(self):
        pass

    def x_axis(self):
        pass

    def y_axis(self):
        pass

    def z_axis(self):
        pass


class Gyroscope(Downhole):
    def __init__(self):
        pass

    def x_axis(self):
        pass

    def y_axis(self):
        pass

    def z_axis(self):
        pass






    

    