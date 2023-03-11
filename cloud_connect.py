import paho.mqtt.client as mqtt
# import wiotp.sdk.application
import json


device_type = "RaspberryPi"
device_id = "Device0001"
org_id = "flhgbn"

url = "{}.messaging.internetofthings.ibmcloud.com".format(org_id)
port = 8883
client_id = "d:{}:{}:{}".format(org_id, device_type, device_id)

topic_name = "iot-2/evt/sensor_data/fmt/json"

username = "use-token-auth"
token = "Device0001"

def on_connect(client, userdata, flags, rc):
        print("Connecting to... " + url)
        print("Connection returned result: " + mqtt.connack_string(rc))

def on_disconnect(client, userdata, rc):
        print("Disconnected from... " + url)

def on_publish(client, userdata, mid):
        print("Published a message: " + str(mid))

def on_log(client, userdata, level, buf):
        print("LOG: ", buf)

# Create the client instance
client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# debug line
#client.on_log = on_log

try:
    client.username_pw_set(username=username, password=token)
    client.tls_set()
    client.connect(url, port, 60)
    client.loop_start()

# =============================================================================
#     # options = wiotp.sdk.application.parseEnvVars()
#     # appClient = wiotp.sdk.application.ApplicationClient(options)
#     myConfig = { 
#         "auth" {
#             "key": "a-org1id-y67si9et"
#             "token": "Ab$76s)asj8_s5"
#         }
#     }
#     appClient = wiotp.sdk.application.ApplicationClient(config=myConfig)
#     
#     
#     # Configure the binding
# # =============================================================================
# #     serviceBinding = {
# #       "name": "mycloudant",  "type": "cloudant", 
# #       "credentials": { 
# #         "host": "8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix.cloudantnosqldb.appdomain.cloud", 
# #         "port": 443, 
# #         "username": "8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix", 
# #         "password": "Z9YhLhqkCJr0cFqsErZnzrm0uuCxExZUWGfx2mmByz16"
# #       }
# #     }
# # =============================================================================
# 
#     serviceBinding = {
#       "name": "mycloudant",  "type": "cloudant", 
#       "credentials": {
#         "apikey": "Z9YhLhqkCJr0cFqsErZnzrm0uuCxExZUWGfx2mmByz16",
#         "host": "8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix.cloudantnosqldb.appdomain.cloud",
#         "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloudantnosqldb:au-syd:a/5dfe20dbe2334ee6a7067a3a0704bedc:41f88fcb-117f-4edc-8d94-485f3e31395b:resource-key:976bdedd-db94-43c2-a63b-8d9ed4b6d084",
#         "iam_apikey_name": "Service credentials-1",
#         "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
#         "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/5dfe20dbe2334ee6a7067a3a0704bedc::serviceid:ServiceId-43e85399-aca3-43f5-95c7-3439de559a53",
#         "url": "https://8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix.cloudantnosqldb.appdomain.cloud",
#         "username": "8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix"
#       }
#     }
#     
#     service = appClient.serviceBindings.create(serviceBinding)
#     # Set up the connector
#     connector = appClient.dsc.create(name="connector1", serviceId=service.id)
#     # Set up destinations
#     # connector.destinations.create(name="events", bucketInterval="MONTH")
#     connector.destinations.create(name="state", bucketInterval="MONTH")
#     # Set up rules
#     # rule1 = connector.rules.createEventRule(name="allevents", destinationName="events", typeId="*", eventId="*")
#     rule2 = connector.rules.createStateRule(name="allstate", destinationName="state", logicalInterfaceId="640a20e0ab911a1e9927f94b")
#         
# =============================================================================
    string = input("Enter the data: ")
    while string!="quit":
        data = json.dumps({'data':string})
        (rc, mid) = client.publish(topic_name, payload=data)
        string = input("Enter the data: ")

except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
except Exception as e:
    print("Connection failed:", e)


client.loop_stop()
client.disconnect()
