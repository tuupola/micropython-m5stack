# Copyright (c) 2019 Mika Tuupola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of  this software and associated documentation files (the "Software"), to
# deal in  the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copied of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
MicroPython I2C driver for IP5306 multi-function power management SOC
"""

__version__ = "0.1.0-dev"

# pylint: disable=import-error
import ustruct
from machine import I2C
from micropython import const
# pylint: enable=import-error

# _SYS_CTL0 = const(0x00)
# _SYS_CTL1 = const(0x01)
# _SYS_CTL2 = const(0x02)
# _CHARGER_CTL0 = const(0x20)
# _CHARGER_CTL1 = const(0x21)
# _CHARGER_CTL2 = const(0x22)
# _CHARGER_CTL3 = const(0x23)
# _REG_READ0 = const(0x70)
# _REG_READ1 = const(0x71)
# _REG_READ2 = const(0x72)
# _REG_READ3 = const(0x77)

_REG_READ4 = const(0x78) # Cannot find documentation?
_BATTERY_75_BIT = const(0b10000000)
_BATTERY_50_BIT = const(0b01000000)
_BATTERY_25_BIT = const(0b00100000)
_BATTERY_0_BIT = const(0b00010000)

# _CHARGE_EN = const(0b00000100) # _REG_READ0
# _CHARGE_FULL = const(0b00000100) # _REG_READ1
# _LIGHT_LOAD = const(0b00000010) # _REG_READ2

class IP5306:
    """Class which provides interface IP5306 multi-function power management SOC."""
    def __init__(self, i2c, address=0x75):
        self.i2c = i2c
        self.address = address

        if self.address not in i2c.scan():
            raise RuntimeError("IP5306 not found in I2C bus")

    @property
    def level(self):
        """
        Battery level in percentage.
        """
        level = self._register_char(_REG_READ4)

        if level & _BATTERY_0_BIT:
            return 0
        elif level & _BATTERY_25_BIT:
            return 25
        elif level & _BATTERY_50_BIT:
            return 50
        elif level & _BATTERY_75_BIT:
            return 75

        return 100

    def _register_char(self, register, value=None, buf=bytearray(1)):
        if value is None:
            self.i2c.readfrom_mem_into(self.address, register, buf)
            return buf[0]

        ustruct.pack_into("<b", buf, 0, value)
        return self.i2c.writeto_mem(self.address, register, buf)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass