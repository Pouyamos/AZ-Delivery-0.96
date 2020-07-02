from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_veml6070 as veml6070

#def main():
    # Instantiate a Vishay UV Sensor on the I2C bus 0
veml6070_sensor = veml6070.VEML6070(0);

    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit, including functions from abpdrrt005pg2a5
def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)



