import paho.mqtt.client as paho
import serial
import time

# https://os.mbed.com/teams/mqtt/wiki/Using-MQTT#python-client

# MQTT broker hosted on local machine
mqttc = paho.Client()
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

# Settings for connection
# TODO: revise host to your IP
host = "192.168.43.162"
topic1= "Gesture"
topic2= "Angle"
i = 0;
# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    global i
    if msg.topic  == topic1:
        print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n");
        s.write("/GestureUI_End/run\r\n".encode())
        print("Start measuring tilt angle...")
        time.sleep(0.5)
        s.write("/AngleMsr/run\r\n".encode())
    elif msg.topic  == topic2:
        if i >= 3:
            s.write("/AngleMsr_End/run\r\n".encode())
            print("Start detecting gesture...")
            time.sleep(0.5)
            s.write("/GestureUI/run\r\n".encode())
            i = 0
        else:
            print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n");
            i = i + 1

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic1)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic1, 0)
print("Connecting to " + host + "/" + topic2)
mqttc.subscribe(topic2, 0)


s.write("/GestureUI/run\r\n".encode())
# Loop forever, receiving messages
mqttc.loop_forever()