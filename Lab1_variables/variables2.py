from microbit import *

def myFunction(value):

    display.show(Image.HAPPY)
    sleep(1000)
    display.show(Image.SAD)
    sleep(1000)
    value = value +2
    for x in range(0,3):
        value = value + 1
        display.show(value)
        sleep(500)
    return value

while True:

    variable = myFunction(3)
    display.show(variable)
    sleep(1000)
