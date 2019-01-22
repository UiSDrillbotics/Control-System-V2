###############################################################
#
#   Take first measurement from every sensor
#
###############################################################

from f1_setup import downhole, input

# Check every sensor value before starting the system
def first_measurement():
    print("Taking first measurements..")
    global downhole
    downhole.new_measurement()
    global input
    input.new_measurement()


    





    

    