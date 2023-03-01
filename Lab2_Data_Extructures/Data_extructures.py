from microbit import *

listd=[1,2,3]
print(listd[2])
ledson  = '00300:''03630:''36963:''03630:''00300' #string
boat1 = Image("05050:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

boat2 = Image("00000:"
              "05050:"
              "05050:"
              "05050:"
              "99999")

boat3 = Image("00000:"
              "00000:"
              "05050:"
              "05050:"
              "05050")

boat4 = Image("00000:"
              "00000:"
              "00000:"
              "05050:"
              "05050")

boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "05050")

boat6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")


all_boatsL = [boat1, boat2, boat3, boat4, boat5, boat6]
#display.show(all_boatsL, delay=200)
#all_boatsL[3]= Image('00300:''03630:''36963:''03630:''00300')
#display.show(all_boatsL, delay=200)
all_boatsT = (boat1, boat2, boat3, boat4, boat5, boat6)
display.show(all_boatsT, delay=200)
all_boatsL.append(Image(ledson))
display.show(all_boatsL, delay=200)
