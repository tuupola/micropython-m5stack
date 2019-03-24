#
# # This file is part of MicroPython M5Stack package
# Copyright (c) 2017-2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-m5stack
#

#pylint: disable=import-error
from machine import I2C, Pin, SPI, Timer
from input import DigitalInput
from ip5306 import IP5306
from micropython import const
import display
import m5stack
#pylint: enable=import-error

BUTTON_Y = const(181)

tft = m5stack.Display()

tft.text(tft.CENTER, 45,        "`7MMM.     ,MMF'       \n")
tft.text(tft.CENTER, tft.LASTY, "  MMMb    dPMM         \n")
tft.text(tft.CENTER, tft.LASTY, "  M YM   ,M MM  M******\n")
tft.text(tft.CENTER, tft.LASTY, "  M  Mb  M' MM .M      \n")
tft.text(tft.CENTER, tft.LASTY, "  M  YM.P'  MM |bMMAg. \n")
tft.text(tft.CENTER, tft.LASTY, "  M  `YM'   MM      `Mb\n")
tft.text(tft.CENTER, tft.LASTY, ".JML. `'  .JMML.     jM\n")
tft.text(tft.CENTER, tft.LASTY, "               (O)  ,M9\n")
tft.text(tft.CENTER, tft.LASTY, "                6mmm9  \n")
tft.text(tft.CENTER, tft.LASTY, "                       \n")
tft.text(tft.CENTER, tft.LASTY, "https://appelsiini.net/")

i2c = I2C(scl=Pin(22), sda=Pin(21))

# Scan for I2C devices:
# 0x56 = Wheel
# 0x68 = MPU6500
# 0x75 = IP5306
devices = map(hex, i2c.scan())
print("I2C devices found:", end=" ")
print(", ".join(devices))

battery = IP5306(i2c)
tft.text(tft.RIGHT, 2, str(battery.level) + "%")

def button_handler_a(pin, pressed):
    if pressed is True:
        tft.text(
            tft.CENTER, BUTTON_Y, "> Button A pressed.     "
        )
        m5stack.tone(1800, duration=10, volume=1)
    else:
        tft.text(
            tft.CENTER, BUTTON_Y, "> Button A released.    "
        )
        m5stack.tone(1300, duration=10, volume=1)

def button_handler_b(pin, pressed):
    if pressed is True:
        tft.text(
            tft.CENTER, BUTTON_Y, "> Button B pressed.     "
        )
        m5stack.tone(2000, duration=10, volume=1)
    else:
        tft.text(
            tft.CENTER, BUTTON_Y, "> Button B released.    "
        )
        m5stack.tone(1500, duration=10, volume=1)

def button_handler_c(pin, pressed):
    if pressed is True:
        tft.text(
            tft.CENTER, BUTTON_Y, "> Button C pressed.     "
        )
        m5stack.tone(2200, duration=10, volume=1)
    else:
        tft.text(
            tft.CENTER, BUTTON_Y, "> Button C released.    "
        )
        m5stack.tone(1800, duration=10, volume=1)

a = m5stack.ButtonA(callback=button_handler_a)
b = m5stack.ButtonB(callback=button_handler_b)
c = m5stack.ButtonC(callback=button_handler_c)

def battery_level(timer):
    tft.text(tft.RIGHT, 2, str(battery.level) + "%")

timer_0 = Timer(0)
timer_0.init(period=5000, mode=Timer.PERIODIC, callback=battery_level)
