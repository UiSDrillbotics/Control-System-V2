# Control-System-V2
Restructured version of the Control-System repository

## Starting the system
The main function is located in the `__init__.py` file. This file initializes the system and starts the operating loop.

## System structure
The parent function of every file is called in this order:
- Setup
- Get First Measurement
- Loop:
  - Get New Measurement
  - Math Calculations
  - Calculate And Set Motor Power
  - Plot Data
- Close Motors And Sensors

### Setup
Initialize system with sensors and motors. Connect to data acquisition system and prepare for start. Located in the file `f1_setup.py`.

### Get First Measurement
Take first measurement from every sensor. Check every sensor value before starting the system. Located in the file `f2_first_measurement.py`.

### Get New Measurement 
Take new measurement from every sensor. Checking values for all sensors. Called from inside a loop. Located in the file `f3a_new_measurement.py`.

### Math Calculations
Do math calculations based on sensor data. Calculations turn sensor readings into usable data. E.g. weight on bit, angle. Located in the file `f3b_math_calculations.py`.

### Calculate And Set Motor Power
Calculate and set motor power. Send new signal to engines. Any output filters should be applied here. Located in the file `f3c_calculate_and_set_motor_power.py`. 

### Plot Data
Plot data to screen. Output raw or processed data. Might not be called for every loop iteration. Located in the file `f3d_plot_data.py`. 

### Close motors and sensors
Safely stop the system and return to initial state. Located in the file `f4_close_motors_and_sensors.py`. 






