# Rig
Files related to a specific hardware device. Preferably defined as a class for each device. Sub-classes could be used to separate specific components of the system.


## Circulation
Pump system to circulate water in the well. Consist of two pumps that is switched between at a specific interval to avoid overheating. The pumps have no system to determine if they are still running.


## Downhole
Sensor inside the sub. Consists of an Adafruit Trinket M0 and an Adafruit 3-Axis Accelerometer, Gyroscope and Magnetometer combi unit. The Trinket is a micro-controller with Python support. The sensor sends signals using the I2C protocol to the micro-controller. The microcontroller sends the reading using serial over USB-cable to the surface. Each sensor type is divided into a sub-class.


## Hoisting
Adjusts the height and WOB during drilling. Controlled by a set of 3 servo engines. 


## Rotation
Controls the top-drive RPM and torque.