# MicroPython Kitchen Sink for M5Stack

## Display

Light weight wrapper for [Loboris TFT](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display) module which retains all the original api and properties but adds a few helper methods.

```python
import m5stack
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
```

Helper methods for turning the display on and off. Under the hood this just sets `TFT_LED_PIN` high or low.

```python
tft.on()
tft.off()
```

## Buttons

Abstraction for the provided buttons using IRQ. Default is `IRQ_FALLING` ie. when button was pressed. You can also use `IRQ_RISING` and `IRQ_RISING | IRQ_FALLING`.

```python
a = m5stack.ButtonA(
    callback=lambda pin: print("Button A pressed.")
)

b = m5stack.ButtonB(
    trigger=Pin.IRQ_RISING,
    callback=lambda pin: print("Button B released.")
)

c = m5stack.ButtonC(callback=button_handler())

def button_hander(pin):
    print("Button C pressed.")
```
