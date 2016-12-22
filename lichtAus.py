#! /usr/bin/python

from xbee import XBee
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(ser)

while True:
        xbee.send('remote_at',
                  frame_id='1',
                  dest_addr_long='\x00\x13\xA2\x00\x40\xAF\xBB\x52',
                  dest_addr='\xFF\xFE',
                  options='\x02',
                  command='D0',
                  parameter='\x04')
