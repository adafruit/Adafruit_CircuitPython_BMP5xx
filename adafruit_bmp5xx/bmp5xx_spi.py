# SPDX-FileCopyrightText: Copyright (c) 2025 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_bmp5xx.bmp5xx_spi`
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

from adafruit_bus_device import spi_device  # noqa: PLC0415
from adafruit_register_spi.spi_bit import ROBit, RWBit
from adafruit_register_spi.spi_bits import ROBits, RWBits

from adafruit_bmp5xx import create_bmp5xx_class

try:
    from typing import Optional

    from busio import SPI
    from digitalio import DigitalInOut
except ImportError:
    pass


def create_bmp5xx_spi(spi: SPI, cs: DigitalInOut):
    BMP5XX_Class = create_bmp5xx_class(ROBit, RWBit, ROBits, RWBits)
    try:
        spi_device_instance = spi_device.SPIDevice(spi, cs)
    except ValueError:
        raise ValueError(f"No SPI device found.")

    return BMP5XX_Class(spi_device=spi_device_instance)
