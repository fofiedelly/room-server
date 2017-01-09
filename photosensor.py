#!/usr/bin/python

import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0, 0)

light_channel = 0
temp_channel = 1

delay = 1


def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts


def ConvertTemp(data, places):
    temp = ((data * 330)/float(1023))-50
    temp = round(temp, places)
    return temp


def get_light_value():
    light_level = ReadChannel(light_channel)
    light_volts = ConvertVolts(light_level, 2)
    temp_level = ReadChannel(temp_channel)
    temp_volts = ConvertVolts(temp_level, 2)
    temp = ConvertTemp(temp_level, 2)
    return light_level
