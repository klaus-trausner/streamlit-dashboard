import random
import paho.mqtt.client as mqtt

broker = '81.7.10.99'
port = 1883
topic = "test"
client_id = f'streamlit-mqtt-{random.randint(0, 1000)}'
username = 'klaus'
password = 'DHisddS!'

def mqtt_init():

    client = mqtt.Client()
    client.username="klaus"
    client.password="DHisddS!"
    client.connect("81.7.10.99", 1883, 60)
    client.subscribe("test")
    client.publish("test", "Welcome to streamlit")
    client.on_message = on_message

    return client

def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))
     
def on_publish(client, userdata, mid, reason_code, properties):
    print("mid: "+str(mid))     
     
def on_connect(client, userdata, flags, reason_code, properties):
    #print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")
      
def connect_mqtt():
    
    # Set Connecting Client ID
    # client = mqtt.Client(client_id)

    # For paho-mqtt 2.0.0, you need to set callback_api_version.
    client = mqtt.Client(client_id=client_id, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect(broker, port)
    return client