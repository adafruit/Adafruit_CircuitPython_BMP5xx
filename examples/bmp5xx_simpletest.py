# SPDX-FileCopyrightText: Copyright (c) 2025 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time

import board

from adafruit_bmp5xx import BMP5XX

i2c = board.STEMMA_I2C()
bmp = BMP5XX(i2c)
start_time = time.monotonic()

while True:
    if bmp.data_ready:
        print(f"temp F: {bmp.temperature * (9 / 5) + 32} pressure: {bmp.pressure} hPa")
        time.sleep(1)
