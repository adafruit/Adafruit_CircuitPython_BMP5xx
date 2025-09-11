# SPDX-FileCopyrightText: Copyright (c) 2025 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time

import board
from digitalio import DigitalInOut, Direction

from adafruit_bmp5xx.bmp5xx_spi import create_bmp5xx_spi

SEALEVELPRESSURE_HPA = 1013.25

spi = board.SPI()
cs = DigitalInOut(board.D10)
cs.direction = Direction.OUTPUT
cs.value = False
bmp = create_bmp5xx_spi(spi, cs)

bmp.sea_level_pressure = SEALEVELPRESSURE_HPA

while True:
    if bmp.data_ready:
        print(
            f"temp F: {bmp.temperature * (9 / 5) + 32} "
            f"pressure: {bmp.pressure} hPa "
            f"Approx altitude: {bmp.altitude} m"
        )
        time.sleep(1)
