from microbit import *
import utime
import time
from microbit import pin13, pin8, pin12
trigger_pin = pin8
echo_pin = pin12
echo_timeout_us = 5
distance_cm= 100


def get_distance():

    pulse_time=0
    trigger_pin.write_digital(1)
    utime.sleep_us(10)
    trigger_pin.write_digital(0)
    while echo_pin.read_digital() == 0:
        #print("loop")
        pass

    if echo_pin.read_digital()==1:
        start = utime.ticks_us()
        while echo_pin.read_digital() == 1:
            #print("loop1")
            pass

        finish = utime.ticks_us()
        pulse_time = finish - start

    # To calculate the distance we get the pulse_time and divide it by 2
    # the sound speed on air (343.2 m/s), that It's equivalent to
    # 0.034320 cm/us

    distance = pulse_time * 0.034 / 2


    return round(distance)

while(True):

    #while distance_cm >10:

        distance_cm = get_distance()


        print (distance_cm)

   # distance_cm =100


