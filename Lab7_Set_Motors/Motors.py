from microbit import *

car_address=0x010

def motors_speed(left_wheel_speed,right_wheel_speed):
    """

    :param left_wheel_speed:-100～100
    :param right_wheel_speed: -100～100

    """
    left_direction = 0x02 if left_wheel_speed > 0 else 0x01
    right_direction = 0x02 if right_wheel_speed > 0 else 0x01

    left_wheel_speed = left_wheel_speed if left_wheel_speed > 0 else left_wheel_speed * -1
    right_wheel_speed = right_wheel_speed if right_wheel_speed > 0 else right_wheel_speed * -1

    if left_wheel_speed > 100 or left_wheel_speed < -100:
        raise ValueError('speed error,-100~100')
    if right_wheel_speed > 100 or right_wheel_speed < -100:
        raise ValueError('speed error,-100~100')



    i2c.write(car_address, bytearray([0x02, left_direction, left_wheel_speed, 0]))

    i2c.write(car_address, bytearray([0x01, right_direction, right_wheel_speed, 0]))

#i2c.write(car_address, bytearray([0x01, 0x01 ,0, 0]))

motors_speed(0,0)