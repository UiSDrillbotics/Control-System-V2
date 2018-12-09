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
Initialize system with sensors and motors. Connect to data acquisition system and prepare for start. Located in the file `setup.py`.

### Get First Measurement
Take first measurement from every sensor. Check every sensor value before starting the system. Located in the file `first_measurement.py`.

### Get New Measurement 
Take new measurement from every sensor. Checking values for all sensors. Called from inside a loop. Located in the file `new_measurement.py`.

### Math Calculations
Do math calculations based on sensor data. Calculations turn sensor readings into usable data. E.g. weight on bit, angle. Located in the file `math_calculations.py`.

### Calculate And Set Motor Power
Calculate and set motor power. Send new signal to engines. Any output filters should be applied here. Located in the file `calculate_and_set_motor_power.py`. 

### Plot Data
Plot data to screen. Output raw or processed data. Located in the file `plot_data.py`. 





