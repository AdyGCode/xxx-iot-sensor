# XXX IoT Sensor

A core project template for the analysis of current technologies and 
their application to industry - specifically within Internet of Things.

This code base is not complete, but **no** contributions are required.

## General Information

* Free software: Open Software License ("OSL") v. 3.0
* Documentation: To be added


## Features

* Bult-in Hardware Sensor (Raspberry Pi) details monitored and delivered via MQTT
* Temperature, pressure and humidity and other sensor inputs monitored and delivered via MQTT

## Requirements

This code presumes certain hardware is being used.

### Hardware:
* Raspberry Pi 3B or later
* Raspberry SenseHAT

The SenseHAT may be preplaced with the equivalent hardware, but in this case any driver code,
or similar, will need to be created, or installed from the required suppliers.

### Package Requirements

This project requires the following package(s):

* `psutils` at least version 5.8.0
* `piview` at least version 2.0.3
* `paho-mqtt` at least version 1.5.1

Remaining packages are Python 'built-ins'.

### Package Installation

The requirements above may be installed using:

```shell
pip3 install PACKAGE_NAME
```
or using the PyCharm Project Preferences


## Credits


## Copyright

Copyright Adrian Gould, 2021 onwards. 
Licensed under the Open Software License version 3.0

Please credit the author whenever this code is used in any capacity.
