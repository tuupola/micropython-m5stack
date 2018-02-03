# This file is part of MicroPython M5Stack package
# Copyright (c) 2017-2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-m5stack

from machine import Pin, SPI # pylint: disable=import-error
from input import DigitalInput # pylint: disable=import-error
import display # pylint: disable=import-error
import m5stack # pylint: disable=import-error

button_a = DigitalInput(
    Pin(m5stack.BUTTON_A_PIN, Pin.IN),
    callback = lambda pin: tft.text(
        tft.CENTER, tft.LASTY, "> Button A pressed.    ")
    )

button_b = DigitalInput(
    Pin(m5stack.BUTTON_B_PIN, Pin.IN),
    callback=lambda pin: tft.text(
        tft.CENTER, tft.LASTY, "> Button B pressed.    "
    )
)

button_c = DigitalInput(
    Pin(m5stack.BUTTON_C_PIN, Pin.IN),
    callback=lambda pin: tft.text(
        tft.CENTER, tft.LASTY, "> Button C pressed.    "
    )
)

# power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
# power.value(1)

tft = m5stack.TFT()

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
