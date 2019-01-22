import serial

# Raw data identifiers
ACC_X, ACC_Y, ACC_Z, MAG_X, MAG_Y, MAG_Z, GYR_X, GYR_Y, GYR_Z, TEMP = range(10)
COM_PORT = 'COM12'
BAUD_RATE = 9600
WINDOW_SIZE = 20

class Downhole:

    def __init__(self):
        # Open communication to the microcontroller
        self.serial = serial.Serial(COM_PORT, BAUD_RATE)
        self.accelerometer = Accelerometer()
        self.magnetometer = Magnetometer()
        self.gyroscope = Gyroscope()
        self.window_counter = 0
        self.window = [0 * 10] * WINDOW_SIZE
        print("Downhole initialized")

    def new_measurement(self):
        # Get raw sensor data and store in the object itself
        # Send request to sensor
        self.serial.write(bytes(0x04))
        serial_data = [0] * 10
        # Read incoming bytes. Each measurement is 16 bit (2 bytes)
        for i in range(10):
            serial_data[i] = int.from_bytes(self.serial.read(2), byteorder='little', signed=True)
        
        self.serial.flushInput()
        self.serial.flushOutput()

        # Keep track of recent values
        self.window[self.window_counter] = serial_data
        self.window_counter += 1
        if self.window_counter % WINDOW_SIZE != self.window_counter:
            self.window_counter = 0


    def math_calculations(self):
        pass
        

class Accelerometer(Downhole):
    def __init__(self):
        self._x_axis = 0
        self._y_axis = 0
        self._z_axis = 0

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
   