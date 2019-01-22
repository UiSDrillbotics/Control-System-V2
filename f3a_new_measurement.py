###############################################################
#
#   Take new measurement from every sensor
#
###############################################################
from f1_setup import downhole

# Checking values for all sensors. Called from inside a loop
def new_measurement():
    # print("Taking new measurement..")
    # Read the downhole sensors
    downhole.new_measurement()
    pass

    


