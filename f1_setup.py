###############################################################
#
#   Initialize system with variables, constants, sensors and motors
#
###############################################################


#-------------------Set global variables-------------------
running = True



#-------------------Set global constants-------------------
FREQUENCY = 100
PLOT_FREQUENCY = 1
PLOT_PERIOD = 1/PLOT_FREQUENCY
PERIOD = 1/FREQUENCY


# Connect to data acquisition system and prepare for start
# The setup process has its own sub-states
# 1. Just started
# 2. Calibrating
# 3. Start drilling state

def setup():
    print("Initializing the control system..")

    