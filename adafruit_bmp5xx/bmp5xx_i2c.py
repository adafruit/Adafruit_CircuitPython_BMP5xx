# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2025 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_bmp5xx.bmp5xx_i2c`
================================================================================

CircuitPython library for the BMP580 / BMP581 / BMP585 / etc barometric pressure sensors.


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**

`Purchase BMP580 from the Adafruit shop <http://www.adafruit.com/products/6411>`_
`Purchase BMP581 from the Adafruit shop <http://www.adafruit.com/products/6407>`_
`Purchase BMP585 from the Adafruit shop <http://www.adafruit.com/products/6413>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads


* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
* Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_register.i2c_bit import ROBit, RWBit
from adafruit_register.i2c_bits import ROBits, RWBits

from adafruit_bmp5xx import DEFAULT_ADAFRUIT_ADDR, create_bmp5xx_class

try:
    from typing import Optional

    from busio import I2C
    from digitalio import DigitalInOut
except ImportError:
    pass


def create_bmp5xx_i2c(i2c: I2C, address: int = DEFAULT_ADAFRUIT_ADDR):
    BMP5XX_Class = create_bmp5xx_class(ROBit, RWBit, ROBits, RWBits)
    try:
        i2c_device_instance = I2CDevice(i2c, address)
    except ValueError:
        raise ValueError(f"No I2C device found.")

    return BMP5XX_Class(i2c_device=i2c_device_instance)
