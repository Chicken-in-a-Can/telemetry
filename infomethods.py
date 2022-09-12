#!/usr/bin/python
import os

class Network:
    def netlist():
        network_list = os.popen("nmcli device wifi list").read()
        return network_list
class Devices:
    def devlist():
        device_list = os.popen("lsusb | grep -v \"Linux Foundation\"").read()
        return device_list
