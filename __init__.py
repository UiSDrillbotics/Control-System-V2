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
from time import time, sleep


# Initializes and starts the operations loop
aborted = False
frequency = 1000
plot_frequency = 1
plot_interval = int(frequency / plot_frequency)
 

period = 1/frequency

loop_count = 0

setup()
first_measurement()

# Keep track of the 
starttime = time()
while not aborted:
    cur_time = time()
    print(cur_time)
    loop_count += 1
    new_measurement()
    math_calculations()
    calculate_and_set_motor_power()
    if loop_count % plot_interval == 0:
        plot_data()
    # print(time() - cur_time)
    # Hold the loop until new meassurement
    # A while loop occupying the processor is much more accurate than sleep
    while time() - starttime - loop_count * period < period:
        pass


close_motors_and_sensors()











