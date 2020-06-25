#!/usr/bin/python

from Adafruit_BMP085 import BMP085
import paho.mqtt.client as mqtt #import the client1
import bh1750
from time import sleep
import mine

import Adafruit_DHT as dht
from time import sleep

#Set DATA pin
DHT = 4
f = open("demofile2.csv", "w")
f.write("Staring measurement" + "\n")
f = open("demofile2.csv", "a+")
"""
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    data["time"]=tnow
    data["topic"]=topic
    data["message"]=msg

broker_address="adveisorgroup2.lsr.ei.tum.de"
print("creating new instance")
client = mqtt.Client("Pooz") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
"""

try:

	while True:

		bmp = BMP085(0x77)
		temp = bmp.readTemperature()
		pressure = bmp.readPressure()
		altitude = bmp.readAltitude()
		lightLevel=bh1750.readLight()
		
		print ("Temperature: %.2f C" % temp)
		print ("Pressure:    %.2f hPa" % (pressure / 100.0))
		print ("Altitude:    %.2f" % altitude)
		h,t = dht.read_retry(dht.DHT22, DHT)
		print('Temp={0:0.1f}*C \nHumidity={1:0.1f}%\n\n'.format(t,h))
		print("Light Level : " + format(lightLevel,'.2f') + " lx")
			
		if int(temp) > 30:
			print ("FIRE DETECTED!\n CALL EMERGENCY!\nFIRST SAVE YOUR LIFE THEN OTHERS!")

		mine.write(h, temp, pressure, lightLevel)
#		f.write("Temperature: {}, Pressure: {}, Altitude: {}, Humidity: {}, Light: {}".format(temp, pressure, altitude, h, lightLevel))		

		#print("Subscribing to topic","house/bulbs/bulb1")
		#client.subscribe("house/bulbs/bulb1")
	#	print("Publishing message to topic","house/bulbs/bulb1")
#		client.publish("house/bulbs/bulb1",h)
#		time.sleep(20) # wait


    #    	print("Publishing message to topic","pooz/")
#                client.publish("pooz/temperature",str(round(t,2)))
 #               client.publish("pooz/humidity",str(round(h,2)))
  #              client.publish("pooz/pressure",str(round(pressure,2)))
   #             client.publish("pooz/lightlevel",str(round(lightLevel,2)))

		sleep(2)


except KeyboardInterrupt:
	print("Ended")
#	client.loop_stop() #stop the loop


