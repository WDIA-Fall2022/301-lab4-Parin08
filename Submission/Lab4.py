# Parin Patel
# 040882160

# Professor I wasn't sure which package I have to keep in final submission so I have put regular package and comment package which was good for Pi.


# Pi version import
# from sense_emu import SenseHat

from sense_hat import SenseHat

import time

s = SenseHat()
s.low_light = True

# Passing default arguments instead of global variables
def trinket_logo(G=(0, 255, 0), Y=(255, 255, 0), B=(0, 0, 255), O=(0, 0, 0)):
    logo = [
        O, O, O, O, O, O, O, O,
        O, Y, Y, Y, B, G, O, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        O, Y, Y, Y, B, G, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def raspi_logo(G=(0, 255, 0), R=(255, 0, 0), O=(0, 0, 0)):
    logo = [
        O, G, G, O, O, G, G, O,
        O, O, G, G, G, G, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
    ]
    return logo


def plus(W=(255, 255, 255), O=(0, 0, 0)):
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def equals(W=(255, 255, 255), O=(0, 0, 0)):
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def heart(P=(255, 105, 180), O=(0, 0, 0)):
    logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def elephant(o=(0, 0, 0), c1=(220, 220, 220), c2=(255, 255, 255)):
    logo = [
        o, o, c1, c1, o, o, o, o,
        o, c1, c1, c1, c1, c1, c1, o,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, c1, c1, c1, c1, c1, c1, c1,
        c1, c2, c2, c1, c1, c1, c1, c1,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, o, c1, c1, o, c1, c1, o,
        c1, o, c2, c1, o, c2, c1, o,
    ]

    return logo



# Function which will ask user to get input an show appropriate pattern
def getChoice():
    num = 7
    # Checking number is not 0 Then ask user again and again same selection menu
    while num != 0:
        # Printing choices
        num = input("Please enter your selection. \n\n 1. Logo \n 2.Plus sign \n 3.Equals sign \n 4.Raspberry \n 5.Heart \n 6.Elephant \n 0.Exit \n")
        # Trying to check input is number and if it is number then in appropriate range
        try:
            if int(num) >= 8 or int(num) < 0:
                print("Invalid input -number out of range \n")
            else:
                # Show assosiate pattern
                print("Execute program")
                if int(num) == 1:
                    s.set_pixels(trinket_logo())
                    time.sleep(.75)
                elif int(num) == 2:
                    s.set_pixels(plus())
                    time.sleep(.75)
                elif int(num) == 3:
                    s.set_pixels(raspi_logo())
                    time.sleep(.75)
                elif int(num) == 4:
                    s.set_pixels(equals())
                    time.sleep(.75)
                elif int(num) == 5:
                    s.set_pixels(heart())
                    time.sleep(.75)
                elif int(num) == 6:
                    s.set_pixels(elephant())
                    time.sleep(.75)
        # If user enter String then it will print this except block
        except:
            print("Invalid input please try again. Try to use numbers. \n")

# Calling function
getChoice()