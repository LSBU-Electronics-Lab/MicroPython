#https://create.withcode.uk/
###
from microbit import *
import time

fl = 1.8
strfl=str(fl)
ledson  = '00300:''03630:''36963:''03630:''00300' #string

sleep(2000)
display.show(Image(ledson))

sleep(1000)

display.show(Image.HAPPY)

display.scroll(strfl)

print("Hello world")

