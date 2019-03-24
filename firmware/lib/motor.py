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
MicroPython I2C driver for M5Stack wheel
"""

__version__ = "0.1.0-dev"

# pylint: disable=import-error
import ustruct
from machine import I2C
from micropython import const
# pylint: enable=import-error

_REG_MOTOR = const(0x00)
_REG_ENCODER = const(0x04)

class Motor:
    """Class which provides interface to M5Stack wheel."""
    def __init__(self, i2c, address=0x56):
        self.i2c = i2c
        self.address = address

        if self.address not in i2c.scan():
            raise RuntimeError("M5Stack wheel not found in I2C bus")

    @property
    def encoder(self, buf=bytearray(4)):
        """
        Return the change in motor encoder values since last read.
        """
        self.i2c.readfrom_mem_into(self.address, _REG_ENCODER, buf)
        raw = ustruct.unpack("<hh", buf)
        return -1 * raw[0], raw[1]

    def speed(self, left, right, buf=bytearray(4)):
        """
        Set the left and right motor speeds.

        :param int left: Value between -255 and 255
        :param int right: Value between -255 and 255
        """
        ustruct.pack_into("<hh", buf, 0, int(left), int(right))
        self.i2c.writeto_mem(self.address, _REG_MOTOR, buf)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass