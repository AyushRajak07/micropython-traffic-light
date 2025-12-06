from machine import Pin, SoftI2C
from time import sleep
from ssd1306 import SSD1306_I2C

# LED setup
red = Pin(5, Pin.OUT)
yellow = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)

# I2C for OLED
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

def show_message(text):
    oled.fill(0)          # clear screen
    oled.text(text, 0, 20)
    oled.show()

while True:
    # RED Light
    red.value(1)
    yellow.value(0)
    green.value(0)
    show_message("STOP - RED")
    print("STOP - Red Light ON")
    sleep(5)

    # GREEN Light
    red.value(0)
    yellow.value(0)
    green.value(1)
    show_message("GO - GREEN")
    print("GO - Green Light ON")
    sleep(5)

    # YELLOW Light
    red.value(0)
    yellow.value(1)
    green.value(0)
    show_message("WAIT - YELLOW")
    print("WAIT - Yellow Light ON")
    sleep(2)
