from microbit import *
import time

x=2
y=2
value=6

ledsoff  = '00000:''00000:''00000:''00000:''00000' #string
ledson  = '00300:''03630:''36963:''03630:''00300' #string
########while###############
while not button_a.is_pressed():
##########if###############################
    if button_b.is_pressed():
        display.show(Image(ledson))
        time.sleep(3)
        sleep(3000)
        display.show(Image.HAPPY)
        time.sleep(32)
        display.show(Image(ledsoff))

        display.set_pixel(0, 0, 9)
        time.sleep(2)
        display.clear()
        #
    else:
        display.show(Image.SAD)
        #time.sleep(2)
        #display.clear()



##########for###############################
for x in range(5):
   display.clear()
   display.set_pixel(x, y, 9)
   sleep(500)

