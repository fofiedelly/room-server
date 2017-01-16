"""
Room Server Code
"""
from flask import Flask
from photosensor import get_light_value
from time import sleep
from flask_cors import CORS, cross_origin
from xbee import XBee
import serial
import time

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/status/<module>")
def get_status(module):
    """
    Get module status, for the light is to return the status of the light
    """
    if module == "light":
        get_light_status()


@app.route('/status/photo')
def get_light_brightness():
    """
    Get the status of the photosensor
    """
    val = []

    val.append(get_light_value())
    sleep(1)
    val.append(get_light_value())
    sleep(1)
    val.append(get_light_value())
    average = sum(val) / len(val)
    return str(average)


@app.route('/licht/an')
def licht_an():
    """
    Get module status, for the light is to return the status of the light
    """
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    xbee = XBee(ser)
    xbee.send('remote_at',
              frame_id='1',
              dest_addr_long='\x00\x13\xA2\x00\x40\xAF\xBB\x52',
              dest_addr='\xFF\xFE',
              options='\x02',
              command='D0',
              parameter='\x05')


@app.route('/licht/aus')
def licht_aus():
    """
    Get module status, for the light is to return the status of the light
    :return:
    """
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    xbee = XBee(ser)
    xbee.send('remote_at',
              frame_id='1',
              dest_addr_long='\x00\x13\xA2\x00\x40\xAF\xBB\x52',
              dest_addr='\xFF\xFE',
              options='\x02',
              command='D0',
              parameter='\x04')



def get_light_status():
    """
    Get module status, for the light is to return the status of the light
    """
    print "Zbee command have to be sent hier"


def licht_aus():
    """
    Get module status, for the light is to return the status of the light
    """
    print "ZBee command have to be sent here"


if __name__ == "__main__":
    app.run()
