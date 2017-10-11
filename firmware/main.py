from ili934x import ILI9341, color565
from machine import Pin, SPI
from input import DigitalInput
import m5stack

button_a = DigitalInput(
    Pin(m5stack.BUTTON_A_PIN, Pin.IN, Pin.PULL_DOWN),
    callback = lambda pin: display.print("Button A pressed."))

button_b = DigitalInput(
    Pin(m5stack.BUTTON_B_PIN, Pin.IN, Pin.PULL_DOWN),
    callback=lambda pin: display.print("Button B pressed."))

button_c = DigitalInput(
    Pin(m5stack.BUTTON_C_PIN, Pin.IN, Pin.PULL_DOWN),
    callback=lambda pin: display.print("Button C pressed."))

power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
power.value(1)

spi = SPI(
    -1,
    baudrate=1200000,
    miso=Pin(m5stack.TFT_MISO_PIN),
    mosi=Pin(m5stack.TFT_MOSI_PIN),
    sck=Pin(m5stack.TFT_CLK_PIN))

display = ILI9341(
    spi,
    cs=Pin(m5stack.TFT_CS_PIN),
    dc=Pin(m5stack.TFT_DC_PIN),
    rst=Pin(m5stack.TFT_RST_PIN))

display.fill(color565(0xff, 0x00, 0x00))
display.fill(color565(0x00, 0x00, 0x00))

display.print("Hello world!")

i = 0
while i < 40:
    display.print("Foo bar {}!".format(i))
    i = i + 1
