# Created By Bob-Teh777

from machine import Pin, SoftI2C, ADC
import ssd1306
import gfx
from time import sleep
import random as ran
import sys
game = True
# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
button = Pin(36, Pin.IN)
def drawPipe(ob1, ob2):
    draw.fill_rect(ob1[0], ob1[1], ob1[2], ob1[3], 1)
    draw.fill_rect(ob2[0], ob2[1], ob2[2], ob2[3], 1)
    return
def movePipe(ob1, ob2):
    if ob1[0] > 128 and ob2[0] > 128:
        ob1[0] = 0
        ob2[0] = 0
        ob1[3] = ran.randint(0, 30)
        ob2[1] = ran.randint(40, 64)
    else:
        ob1[0] += 1
        ob2[0] += 1
    return ob1, ob2
def loseScreen(score, value):
    oled.fill(0)
    oled.text('SCORE: ' + str(score), 0, 0, 1)
    oled.show()
    while not value:
        value = not button.value()
        if value == True:
            break
value = not button.value()
while game:
    # Game Variables
    x = 20
    y = 26
    score = 0
    ob1 = [5, 0, 2, ran.randint(0, 30)]
    ob2 = [5, ran.randint(40, 64), 2, 34]
    gravity = 1
    speed = 0.001
    # Screen Variables
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    draw = gfx.GFX(oled_width, oled_height, oled.pixel)
    oled.fill(0)
    oled.text('Press 1 To START', 0, 0)
    oled.show()
    while True:
        value = not button.value()
        if value == True:
            oled.fill(0)
            oled.text('STARTING...', 0, 0)
            oled.show()
            break
    sleep(1)
    while True:
        value = not button.value()
        oled.fill(0)
        draw.fill_rect(x, y, 10, 10, 1)
        oled.text(str(score), 0, 0)
        drawPipe(ob1, ob2)
        movePipe(ob1, ob2)
        oled.show()
        if y > 52:
            y = y
        else:
            y += gravity
        if value == True:
            y -= 2
        sleep(speed)
        if ((y + 10) < ob1[1] or (y + 10) > ob2[1]) and (x == ob1[0] or x == ob2[0]):
            loseScreen(score, value)
            break
        if x == ob1[0] or x == ob2[0]:
            score += 1
        if y < 0:
            y += 1
