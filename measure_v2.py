#!/usr/bin/python

from Adafruit_BMP085 import BMP085
import paho.mqtt.client as mqtt #import the client1
import bh1750
import datetime
from time import sleep
import Adafruit_DHT as dht
#import mine
import RPi.GPIO as GPIO

channel_fire=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_fire, GPIO.IN)



def callback(channel):
	global temp
        if int(temp) > 33:
                print('flame detected')
		client.publish("pooz/fireflag","1")

GPIO.add_event_detect(channel_fire ,GPIO.RISING,bouncetime=300)
GPIO.add_event_callback(channel_fire ,callback)


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



def main():

    #Set DATA pin
    DHT = 4
    f = open("demofile2.csv", "w")
    f.write("Staring measurement" + "\n")
    f = open("demofile2.csv", "a+")


    try:

    	global temp
    	client.publish("pooz/measuring","1")

	while True:

		if GPIO.input == False:

			client.publish("pooz/fireflag","0")

    		bmp = BMP085(0x77)
    		temp = bmp.readTemperature()
    		pressure = bmp.readPressure()
    		altitude = bmp.readAltitude()
    		#lightLevel=bh1750.readLight()
    		now = datetime.datetime.now()


    		print ("Temperature: %.2f C" % temp)
    		print ("Pressure:    %.2f hPa" % (pressure / 100.0))
    		print ("Altitude:    %.2f" % altitude)
    		h,t = dht.read_retry(dht.DHT22, DHT)
    		print('Temp={0:0.1f}*C \nHumidity={1:0.1f}%\n\n'.format(t,h))
    		print("Light Level : " + format(lightLevel,'.2f') + " lx")


    #		f.write("Date: {}, Temperature: {}, Humidity: {}, Light: {}".format(now.strftime("%Y-%m-%d %H:%M:%S"),t, h, lightLevel))

    		print("Publishing message to topic","pooz/")
    		client.publish("pooz/temperature",str(round(temp,2)))
    		client.publish("pooz/humidity",str(round(h,2)))
    		client.publish("pooz/pressure",str(round(pressure,2)))
    		client.publish("pooz/lightlevel",str(round(lightLevel,2)))
		client.publish("pooz/fireflag","0")

    		sleep(3)


    except KeyboardInterrupt:
    	client.publish("pooz/measuring","0")
	print("Ended")
    	client.loop_stop() #stop the loop
	gpio.cleanup()

if __name__=='__main__':

	main()
