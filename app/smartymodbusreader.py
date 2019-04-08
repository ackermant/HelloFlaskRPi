from app import app
from flask import Flask
import configparser
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import pymodbus.client.sync

class MyConnection():
    # Read configuration file to get Smarty IP address
    config = configparser.ConfigParser()
    config.read('config.ini')
    smartyip = config['DEFAULT']['SMARTY_IP']
    TRIPLC = pymodbus.client.sync.ModbusTcpClient(host=smartyip, port=502)

    def testconnection(self):
        testconnect = self.TRIPLC.connect()
        return testconnect

    def readregister(self, registerno):
#        regnum = registerno.get_text()
        regOffset = int(registerno) - 1
        # register number in parameter corresponds to index 0, eg. (5081, 1) reads register 5082
        rr1 = self.TRIPLC.read_holding_registers(regOffset, 1)
        # rr1 array starts with 0
        currentVal = str(rr1.getRegister(0))
        return currentVal