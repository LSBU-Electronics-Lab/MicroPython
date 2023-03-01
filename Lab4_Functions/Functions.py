from microbit import *
from random import randint

def ledMoving(y):
    counter=0
    for x in range(0,5):# the loop needs to run to 5 to include 4 ## leds go from 0 to 4

        counter=counter+1
        counter1 = counter + 2
        counter2 = counter + 3
        counter3 = counter + 4
        listC = [counter1,counter2,counter3]

        display.clear()
        display.set_pixel(x, y, 9)
        sleep(500)
        if(x==2):
            return counter,listC
    return counter


#ledMoving(2)
#display.clear()
#ledMoving(0)
#display.clear()


#finalValue=ledMoving(randint(0,4))
finalValue,mylist = ledMoving(0)


print("Counter is {}".format(finalValue))
print("List is ",mylist)

#display.set_pixel(0, 0, 9)
#time.sleep(3)
#display.set_pixel(4, 4, 9)




