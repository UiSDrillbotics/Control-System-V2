###############################################################
#
#   Control system main file
#
###############################################################

from setup import *
from first_measurement import *
from new_measurement import *
from math_calculations import *
from calculate_and_set_motor_power import *
from plot_data import *
from close_motors_and_sensors import *
from time import perf_counter


# Initializes and starts the operations loop
running = True

FREQUENCY = 100
PLOT_FREQUENCY = 1
PLOT_PERIOD = 1/PLOT_FREQUENCY
PERIOD = 1/FREQUENCY

setup()
first_measurement()

t = perf_counter()
while running:
    print(perf_counter())
    t += PERIOD
    
    # Execute operations
    new_measurement()
    math_calculations()
    calculate_and_set_motor_power()
    plot_data()

    # Hold the loop until new meassurement
    # This approach is more accurate than a sleep()
    while t - perf_counter() > 0:
        pass

# System is no longer running
close_motors_and_sensors()











