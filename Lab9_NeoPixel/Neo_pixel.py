from microbit import *
import neopixel
import random
bottomLights = neopixel.NeoPixel(pin15, 2)
left_Nlight =0
right_Nlight = 1

def neo_lights(left,right,LR,LG,LB,RR,RG,RB):


        bottomLights[left]=(LR,LG,LB)
        bottomLights[right] = (RR,RG,RB)
        bottomLights.show()

neo_lights(left_Nlight,right_Nlight,255,0,0,0,255,0)