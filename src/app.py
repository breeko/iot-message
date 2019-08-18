from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import config
from subscriptions import subs

def setup_mqtt_client():
    camMQTTClient = AWSIoTMQTTClient(config.clientId)
    camMQTTClient.configureEndpoint(config.host, config.port)
    camMQTTClient.configureCredentials(config.rootCAPath, config.privateKeyPath, config.certificatePath)

    camMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    camMQTTClient.configureOfflinePublishQueueing(-1)   # Infinite offline Publish queueing
    camMQTTClient.configureDrainingFrequency(2)         # Draining: 2 Hz
    camMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
    camMQTTClient.configureMQTTOperationTimeout(5)      # 5 sec

    camMQTTClient.connect()
    return camMQTTClient

def subscribe(client):
    for topic, func in subs.items():
        client.subscribe(topic, 1, func)

if __name__ == "__main__":
    client = setup_mqtt_client()
    subscribe(client)
    print("Listening...")
    while True:
        pass
