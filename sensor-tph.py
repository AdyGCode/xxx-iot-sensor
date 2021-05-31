'''
Project:    xxx-iot-sensor
Filename:   sensor-tph.py
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


def main():
    import datetime
    import json
    import time

    import paho.mqtt.client as mqtt
    from piview.Host import Host
    from piview.Network import Network

    # MQTT Server details
    mqtt_server = "127.0.0.1"  # Default to local machine
    mqtt_port = 1883  # Default port used by MQTT
    mqtt_time_alive = 60  # Keep Alive time

    #  Get the Pi name, model, revision, serial number and MAC
    sensor_name = Host.name()
    sensor_serial = Host.serial()
    sensor_mac = Network.mac()
    sensor_model = Host.model()
    sensor_revision = Host.revision()

    mqtt_sensor_name = f"{sensor_name}-{sensor_serial}"

    # Define message topic and period between data updates
    topic = "NMTAFE/IoT"
    time_between_updates = 5.0  # seconds

    # set flag for connection status of sensor to MQTT server
    mqtt.Client.connected_flag = False

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("connected OK Returned code=", rc)
            client.connected_flag = True
            # TODO: Use PiView to obtain the sensor data, save to
            #       a variable and then make sure the data is inserted into the
            #       dictionary as shown for the sensor_ip
            sensor_ip = Network.ip()
            # TODO: Add a variable (as defined below) and retrieve the
            #  required details for the Pi using the piview package for
            #  each of the following:
            #       boot_time
            # sensor_ram = Storage.ram()
            #       ram
            #       storage
            #       hw_i2c
            # hw_i2c = Hardware.i2c()
            #       hw_bt
            #       hw_camera
            #       hw_spi

            # Create the data payload to send as the message to the MQTT server
            # TODO: Remember to replace the 'UNKNOWN', 'False' etc with the
            #       correct newly created variable as given above
            data = json.dumps({
                'sensor': mqtt_sensor_name,
                'message': 'connected',
                'model': 'UNKNOWN',
                'ip': sensor_ip,
                'mac': sensor_mac,
                'boot-time': '0000-00-00 00:00:00.0',
                'ram': 0,
                'storage': 0,
                'hw-i2c': False,
                'hw-bt': False,
                'hw-camera': False,
                'hw-spi': False,
                'time': str(datetime.datetime.now())
            })
            client.publish(topic, data)
        else:
            print("Bad connection Returned code=", rc)

    # Create MQTT Client connection and callback hooks
    client = mqtt.Client(mqtt_sensor_name, clean_session=True)
    client.on_connect = on_connect
    client.loop_start()

    # Connect to the MQTT Server
    client.connect(mqtt_server, mqtt_port, mqtt_time_alive)

    print('Waiting for connection to MQTT Server...')
    while not client.connected_flag:  # wait in loop
        time.sleep(1)

    # a short delay before getting first readings
    time.sleep(1)

    while True:
        # TODO: Create the code to give readings for each of the SenseHat
        #       sensors listed below. Replace the strings as needed.
        sensehat_temperature = 'SenseHat Temperature Reading'
        sensehat_pressure = 'SenseHat Pressure Reading'
        sensehat_humidity = 'SenseHat Humidity Reading'
        sensehat_accelerometer = 'SenseHat Accelerometer Reading'
        sensehat_compass = 'SenseHat Compass Reading'

        # Create the JSON string to send to the MQTT server
        data = json.dumps({
            'sensor': mqtt_sensor_name,
            'temperature': sensehat_temperature,
            # TODO: pressure reading key-value pair
            # TODO: humidity reading key-value pair
            # TODO: accelerometer reading key-value pair
            # TODO: compass reading key-value pair
            'time': str(datetime.datetime.now()),
        })

        # Send the topic and data to MQTT Server
        client.publish(topic, data)

        # Display data just delivered
        print(f"Published {topic} : {data}")

        # Sleep until next reading required
        time.sleep(time_between_updates)


if __name__ == '__main__':
    main()
