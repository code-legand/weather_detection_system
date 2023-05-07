import paho.mqtt.client as mqtt
import json

device_type = "RaspberryPi"
device_id = "Device0001"
org_id = "1w95zu"

mqtt_broker = "{}.messaging.internetofthings.ibmcloud.com".format(org_id)
mqtt_port = 8883
mqtt_username = "use-token-auth"
mqtt_token = "Device0001"

topic_name = "iot-2/evt/sensor_data/fmt/json"

def on_connect(client, userdata, flags, rc):
    print("Connected to IBM Watson IoT Platform with result code: " + str(rc))
    client.subscribe(topic_name)

def on_disconnect(client, userdata, rc):
    print("Disconnected from IBM Watson IoT Platform")

def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())

# Create the MQTT client instance
client = mqtt.Client(client_id=device_id)
client.username_pw_set(mqtt_username, password=mqtt_token)

# Set the callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT client loop (non-blocking)
client.loop_start()

# Publish a message to the device
message = json.dumps({'data': 'Hello World'})
client.publish(topic_name, payload=message)

# Disconnect from the MQTT broker
client.loop_stop()
client.disconnect()
