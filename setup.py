###############################################################
#
#   Initialize system with variables, constants, sensors and motors
#
###############################################################


#-------------------Set global variables-------------------
running = True



#-------------------Set global constants-------------------
FREQUENCY = 10
PLOT_FREQUENCY = 1
PLOT_PERIOD = 1/PLOT_FREQUENCY
PERIOD = 1/FREQUENCY


# Connect to data acquisition system and prepare for start
def setup():
    print("Initializing the control system..")

    