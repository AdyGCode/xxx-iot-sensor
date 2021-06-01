'''
Project:    xxx-iot-sensor
Filename:   sensor-system.py
Location:   ./
Author:     STUDENT NAME <STUDENT TAFE EMAIL ADDRESS>
Created:    28/05/21
Purpose:
    This file provides the following features, methods and associated
    supporting code:

    TODO: STUDENT TO DESCRIBE THE PURPOSE OF THIS FILE

Requirements:
    An MQTT Server to act as a 'broker' to accept messages and pass onto
    subscribers to the message topic(s).
    Python 3.6 or later

Required Packages:
    This project requires the following Python Packages to be installed:
        piview
        paho-mqtt
            
'''

import datetime
import json
import time

import paho.mqtt.client as mqtt
from piview.CPU import CPU
from piview.Host import Host
from piview.Network import Network

# TODO: Add the required imports from piview to get the GPU temperature,
#       and other details as needed such as Storage, RAM etc

mqtt_server = "127.0.0.1"
mqtt_port = 1883
mqtt_time_alive = 60
# Define the MQTT topic as given below
topic = "NMTAFE/IoT"

#  Get the Pi name, model, revision, serial number, IP and MAC
sensor_name = Host.name()
sensor_serial = Host.serial()
sensor_mac = Network.mac()
sensor_model = Host.model()
sensor_revision = Host.revision()
sensor_ip = Network.ip()
# create the sensor name for MQTT
mqtt_sensor_name = f"{sensor_name}-{sensor_serial}"

# TODO: Once this module is working correctly, change update frequency to 60.0s
update_frequency = 10.0

mqtt.Client.connected_flag = False


def on_connect(client, userdata, flags, rc):
    '''On connection, give details of the sensor including:
        Name, Serial Number, IP Address, Total RAM, Total Storage, Boot Time
        Hardware statuses (i2c, camera, etc) plus time of connection

    :param client:
    :param userdata:
    :param flags:
    :param rc:
    :return:
    '''
    if rc == 0:
        # Connection successful
        print("connected OK Returned code=", rc)
        client.connected_flag = True
        # TODO: Obtain Sensor's Total RAM from piview.Storage
        sensor_ram = 0
        # TODO: Obtain Sensor's Total Storage from piview.Storage
        sensor_storage = 0
        # TODO: Obtain Sensor's I2C Hardware status from piview.Hardware
        sensor_i2c = False
        # TODO: Obtain Sensor's Bluetooth Hardware status from piview.Hardware
        sensor_bt = False
        # TODO: Obtain Sensor's Camera Hardware status from piview.Hardware
        sensor_camera = False
        # TODO: Obtain Sensor's SPI Hardware status from piview.Hardware
        sensor_spi = False
        # TODO: Obtain Sensor's Boot Time from piview.Host
        sensor_boot_time = '0000-00-00 00:00:00.0'

        # Create the payload data to be sent in the message to the MQTT server
        # TODO: Update the items without variables after a colon (:) (They
        #       have dummy values or strings to provide placeholders.
        #       For example the 'ram' : 0
        #       Should read 'ram' : sensor_ram
        data = json.dumps({
            'sensor': mqtt_sensor_name,
            'message': 'connected',
            'model': 'UNKNOWN',
            'ip': sensor_ip,
            'mac': sensor_mac,
            'boot-time': sensor_boot_time,
            'ram': 0,
            'storage': sensor_storage,
            'hw-i2c': False,
            'hw-bt': False,
            'hw-camera': False,
            'hw-spi': sensor_spi,
            'time': str(datetime.datetime.now()),
        })
        client.publish(topic, data)
    else:
        print("Bad connection Returned code=", rc)


client = mqtt.Client(mqtt_sensor_name, clean_session=True)
client.on_connect = on_connect
client.loop_start()

client.connect(mqtt_server, mqtt_port, mqtt_time_alive)

print('Waiting for connection to MQTT Server...')
while not client.connected_flag:  # wait in loop
    time.sleep(1)

time.sleep(1)
while True:
    # Add sensor CPU Max Load
    sensor_max_load = CPU.max_load()
    # TODO: Add sensor_cpu_temperature - reading from CPU.temperature
    cpu_temperature = 'Sensor CPU Temperature',
    # TODO: Add sensor_gpu_temperature - reading from GPU.temperature
    gpu_temperature = 'Sensor GPU Temperature',
    # TODO: Add sensor_ram
    sensor_free_ram = 'Sensor RAM',
    # TODO: Add sensor_storage
    sensor_storage = 'Sensor Storage',

    # create JSON data to send in message payload
    data = json.dumps({
        'sensor': mqtt_sensor_name,
        'cpu-temp': 'cpu_temperature',
        'gpu-temperature': 'gpu_temperature',
        'cpu-max-load': sensor_max_load,
        'time': str(datetime.datetime.now()),
    })
    client.publish(topic, data)
    print(f"Published {topic} : {data}")
    time.sleep(update_frequency)
