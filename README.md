# XXX IoT Sensor

A core project template for the analysis of current technologies and their application to
industry - specifically within Internet of Things.

This code base is not complete, but **no** contributions are required.

## General Information

* Free software: Open Software License ("OSL") v. 3.0
* Documentation: To be added

## Features

* Built-in Hardware Sensor (Raspberry Pi) details monitored and delivered via MQTT
* SenseHAT Temperature, pressure and humidity and other sensor inputs monitored and delivered 
  via MQTT

## Requirements

This code presumes certain hardware is being used.

### Hardware:

* Raspberry Pi 3B or later
* Raspberry SenseHAT

The SenseHAT may be replaced with the equivalent hardware, but in this case any driver code, or
similar, will need to be created, or installed from the required suppliers.

### Software

### MQTT Server

- anonymous access allowed for this simple example
- default port is 1883

Install using : `sudo apt-get update` followed by `sudo apt-get install mosquitto`

### Package Requirements

This project requires the following package(s):

| Package      | Purpose                            | Recommended Version |
|--------------|------------------------------------|---------------------|
| `paho-mqtt`  | Python MQTT package                | v1.5.1 or later     |
| `piview`     | Raspberry Pi Information package   | v2.0.3 or later     |
| `psutil`     | system utilities                   | v5.8.0 or later     |

Remaining packages are Python 'built-ins'.

### Package Installation

You may install the required packages using the usual methods:

- pip
- PyCharm Python Interpreter settings

#### Installation via PIP

```shell
pip3 install PACKAGE_NAME
```

for example:

```shell
pip3 install SQLAlchemy
```

#### Installation via PyCharm

1. Click File
2. Settings
3. Project: xxx-iot-server settings
4. Select Python Interpreter settings page
5. Click the + to add package
6. Type in package name in search area (eg `SQLAlchemy`)
7. Select the correct package,
8. Click Install package
9. Repeat steps 6-8 for each required package

## Required Software Installation and Configuration

There are a number of items required for this stage. This includes Mosquitto, Python and other
system items.

### Install and Configure Mosquitto on Raspberry Pi

TODO: Create these instructions

## Credits

## Copyright

Copyright Adrian Gould, 2021 onwards. Licensed under the Open Software License version 3.0

Please credit the author whenever this code is used in any capacity.
