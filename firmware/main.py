# This file is part of MicroPython M5Stack package
# Copyright (c) 2017 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-m5stack

from machine import Pin, SPI
from input import DigitalInput
import display
import m5stack

button_a = DigitalInput(
    Pin(m5stack.BUTTON_A_PIN, Pin.IN),
    callback = lambda pin: tft.text(
        tft.CENTER, tft.LASTY, "> Button A pressed.    ")
    )

button_b = DigitalInput(
    Pin(m5stack.BUTTON_B_PIN, Pin.IN),
    callback=lambda pin: tft.text(
        tft.CENTER, tft.LASTY, "> Button B pressed.    ")
    )

button_c = DigitalInput(
    Pin(m5stack.BUTTON_C_PIN, Pin.IN),
    callback=lambda pin: tft.text(
        tft.CENTER, tft.LASTY, "> Button C pressed.    ")
    )

# power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
# power.value(1)

tft = display.TFT()
tft.init(
    tft.ILI9341,
    spihost=tft.HSPI,
    width=320,
    height=240,
    mosi=m5stack.TFT_MOSI_PIN,
    miso=m5stack.TFT_MISO_PIN,
    clk=m5stack.TFT_CLK_PIN,
    cs=m5stack.TFT_CS_PIN,
    dc=m5stack.TFT_DC_PIN,
    rst_pin=m5stack.TFT_RST_PIN,
    backl_pin=m5stack.TFT_LED_PIN,
    backl_on=1,
    speed=2600000,
    invrot=3,
    bgr=True
)

tft.orient(tft.LANDSCAPE)
tft.font(tft.FONT_Small, fixedwidth=True)

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
