# Copyright (C) 2017 The „Zaubertisch“ Authors (see AUTHORS file)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
import time
import RPi.GPIO as GPIO
import random

import Adafruit_WS2801 as adafruit
import Adafruit_GPIO.SPI as SPI

PIXEL_COUNT = 32

SPI_PORT    = 0
SPI_DEVICE  = 0
pixels      = adafruit.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

print("Clean...")
pixels.clear()
pixels.show()

pos = [0,8,16,24,32,40,48,56,64,72,80,88,96,104,112,120,128,136,144,152,160,168,176,184,192,200,208,216,224,232,240,248]

def wheel(pix):
    p = pos[pix]
    pos[pix] += 4
    if p < 85:
        pixels.set_pixel(pix, adafruit.RGB_to_color(p*3, 255-p*3, 0))
    elif p < 170:
        p -= 85
        pixels.set_pixel(pix, adafruit.RGB_to_color(255-p*3, 0, p*3))
    else:
        p -= 170
        pixels.set_pixel(pix, adafruit.RGB_to_color(0, p*3, 255-p*3))
    if pos[pix] >= 255:
        pos[pix] = 0

cnt = 0
while 1==1:
    for i in range(PIXEL_COUNT):
        wheel(i)
        cnt += random.randint(0,1)
        if cnt%16 == 0:
            pixels.set_pixel(random.randint(0,31), adafruit.RGB_to_color(255,255,255))
        pixels.show()
        time.sleep(0.001)
