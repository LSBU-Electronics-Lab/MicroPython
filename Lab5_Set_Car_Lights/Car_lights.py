from microbit import  *

car_address=0x010
left_light=0x04
right_light=0x08

def set_car_lights(light,R,G,B):
    """

            :param light: left_light=0x04  right_light=0x08
            :param R:R 0-255
            :param G:G 0-255
            :param B:B 0-255


            """

    if R > 255 or G > 255 or B > 255:
        raise ValueError

    i2c.write(car_address, bytearray([light, R, G, B]))


try:

    set_car_lights(left_light,300,3,3)
    set_car_lights(right_light,0,255,0)
except ValueError:
    print("There was an error")


