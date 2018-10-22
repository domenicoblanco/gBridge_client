#!/usr/bin/python
# -*- coding: utf-8 -*-
# MQTT 
import paho.mqtt.client as mqtt
# Control GPIO 
import RPi.GPIO as GPIO

import time


# Define Variables
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "gBridge/u68/d112/onoff"

LED1 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
try:
  # Define on_message event function. 
  # This function will be invoked every time,
  # a new message arrives for the subscribed topic 
  def on_message(mosq, obj, msg):
    if(str(msg.topic)==MQTT_TOPIC):
      print(str(msg.topic))
      GPIO.output(LED1,GPIO.HIGH)
      GPIO.output(LED1,GPIO.LOW)
      time.sleep(0.15)
      GPIO.output(LED1,GPIO.HIGH)
      print "Topic: " + str(msg.topic)
      print "QoS: " + str(msg.qos)
      mqttc.publish(MQTT_TOPIC+"/set", 0)
      print "Topic updated"
    if(str(msg.topic)==MQTT_TOPIC+"/set"):
      print("Update status: "+str(msg.payload))

  # Initiate MQTT Client
  mqttc = mqtt.Client()
  # Assign event callback
  mqttc.on_message = on_message
  # Connect with MQTT Broker
  mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
  mqttc.subscribe(MQTT_TOPIC)
  # Continue check the incoming messages
  mqttc.loop_forever()

except KeyboardInterrupt:  
    GPIO.cleanup()
