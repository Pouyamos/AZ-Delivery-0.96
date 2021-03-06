#!/usr/bin/python

from Adafruit_BMP085 import BMP085
import paho.mqtt.client as mqtt #import the client1
import bh1750
import datetime
from time import sleep
import Adafruit_DHT as dht
#import mine
import RPi.GPIO as GPIO
import subprocess



"""
channel_fire=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_fire, GPIO.IN)



def callback(channel):
	global temp
        if int(temp) > 33:
                print('flame detected')
		subprocess.call(['mosquitto_pub', '-t', 'pooz/fireflag', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', "1"])

GPIO.add_event_detect(channel_fire ,GPIO.RISING,bouncetime=300)
GPIO.add_event_callback(channel_fire ,callback)
"""

def main():

    #Set DATA pin
    DHT = 4


    try:

    	global temp
    	subprocess.call(['mosquitto_pub', '-t', 'khan/measuring', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', "1"])

	while True:

		if GPIO.input == False:

			subprocess.call(['mosquitto_pub', '-t', 'khan/fireflag', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', "0"])

    		bmp = BMP085(0x77)
    		temp = bmp.readTemperature()
    		pressure = bmp.readPressure()
    		altitude = bmp.readAltitude()
    		lightLevel=bh1750.readLight()
    		now = datetime.datetime.now()


    		print ("Temperature: %.2f C" % temp)
    		print ("Pressure:    %.2f hPa" % (pressure / 100.0))
    		print ("Altitude:    %.2f" % altitude)
    		h,t = dht.read_retry(dht.DHT22, DHT)
    		print('Temp={0:0.1f}*C \nHumidity={1:0.1f}%\n\n'.format(t,h))
    		print("Light Level : " + format(lightLevel,'.2f') + " lx")


    #		f.write("Date: {}, Temperature: {}, Humidity: {}, Light: {}".format(now.strftime("%Y-%m-%d %H:%M:%S"),t, h, lightLevel))

    		print("Publishing message to topic","khan/")
    		
    		subprocess.call(['mosquitto_pub', '-t', 'khan/temperature', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', str(round(temp, 2))])
		subprocess.call(['mosquitto_pub', '-t', 'khan/humidity', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', str(round(h,2))])
		subprocess.call(['mosquitto_pub', '-t', 'khan/pressure', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', str(round(pressure,2))])
		subprocess.call(['mosquitto_pub', '-t', 'khan/lightlevel', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', str(round(lightLevel,2))])
		#subprocess.call(['mosquitto_pub', '-t', 'khan/fireflag', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', "0"])

    		
    		"""
    		client.publish("pooz/temperature",str(round(temp,2)))
    		client.publish("pooz/humidity",str(round(h,2)))
    		client.publish("pooz/pressure",str(round(pressure,2)))
    		client.publish("pooz/lightlevel",str(round(lightLevel,2)))
		client.publish("pooz/fireflag","0")
		"""
    		sleep(600)


    except KeyboardInterrupt:
    	subprocess.call(['mosquitto_pub', '-t', 'khan/measuring', '-h', 'adveisorgroup2.lsr.ei.tum.de', '-m', "0"])
	print("Ended")
    	client.loop_stop() #stop the loop
	GPIO.cleanup()

if __name__=='__main__':

	main()
