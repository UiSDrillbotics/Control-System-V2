## Downhole
Sensor inside the sub. Consists of an Adafruit Trinket M0 and an Adafruit 3-Axis Accelerometer, Gyroscope and Magnetometer combi unit. The Trinket is a micro-controller with Python support. The sensor sends signals using the I2C protocol to the micro-controller. The microcontroller sends the reading using serial over USB-cable to the surface. Each sensor type is divided into a sub-class.

## DAQ Input
Files related to the Measurement Computing USB-1608GX DAQ system. All system inputs should be performed from functions within this folder.

## DAQ Output
Files related to the Measurement Computing USB-3114 DAQ system. All system hardware outputs should be performed from functions within this folder.
