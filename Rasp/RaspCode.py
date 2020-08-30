import uuid
import json
import paho.mqtt.client as mqtt
import serial, time
arduino = serial.Serial("/dev/ttyS0",9600)
time.sleep(2)

mqtt_user_name = 'oauth2-user'
mqtt_password = 'YOURTOKEN'  # copy and paste here external client id from your account
user_id = 'YOURUSERID'  # copy and paste here your user id
device_id = 'YOURDEVICEID'  # copy and paste here your device id
ind=""

alerts_topic = '/v1/users/{user_id}/in/alerts'.format(user_id=user_id)
acc_norm_datasource_topic = '/v1/users/{user_id}/in/devices/{device_id}/datasources/MOTION'.format(
    user_id=user_id,
    device_id=device_id)

ca_cert_path = 'cacert.crt'


def on_connect(client, userdata, flags, rc):
    print('Connected with result code {code}'.format(code=rc))


def on_message(client, userdata, msg):
    global ind
    ind= json.loads(str(msg.payload.decode("utf-8")))
    #print(ind[0]['probabilityRank'])
    print(ind[0]['name'])
    arduino.write(ind[0]['name'].encode())


def main():
    client = mqtt.Client(client_id=str(uuid.uuid4()), transport='websockets')
    client_iad=str(uuid.uuid4())
    print(client_iad)
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set(ca_certs=ca_cert_path)
    client.username_pw_set(mqtt_user_name, mqtt_password)

    client.connect('ns01-wss.brainium.com', 443)

    client.subscribe(alerts_topic)
    client.subscribe(acc_norm_datasource_topic)

    client.loop_forever()


if __name__ == "__main__":
    main()