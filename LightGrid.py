import time
from neopixel import *

class LightGrid:
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 5
    LED_BRIGHTNESS = 128
    LED_INVERT = False

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.strands = []
        for i in range(height):
            strands[i] = Adafruit_Neopixel(width, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
            strands[i].begin()

    def setPixel(self, row, col, color):
        strands[row].setPixelColor(col, color)
        strands[row].show

    def setGrid(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                strands[i].setPixelColor(j, color)

grid = LightGrid(1, 30)
for i in range(30):
	setPixel(1, i, Color(255, 255, 255))

