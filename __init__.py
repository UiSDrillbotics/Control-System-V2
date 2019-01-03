###############################################################
#
#   Control system main file
#
###############################################################

from f1_setup import *
from f2_first_measurement import *
from f3a_new_measurement import *
from f3b_math_calculations import *
from f3c_calculate_and_set_motor_power import *
from f3d_plot_data import *
from f4_close_motors_and_sensors import *
from time import perf_counter


# Initializes and starts the operations loop
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











