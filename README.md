# Control-System-V2
Restructured version of the Control-System repository

## System structure
The parent function of every file is called in this order:
- Init
- Get First Measurement
- Loop:
  - Get New Measurement
  - Math Calculations
  - Calculate And Set Motor Power
  - Plot Data
- Close Motors And Sensors

### Init
Initialize system with sensors and motors. Connect to data acquisition system and prepare for start. Located in the file `init.py`



