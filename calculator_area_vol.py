"""
    Area, Volume and Capacity calculator
    Alexander Perkins 1/6/24
    Do not copy
"""

#   Imports
from random import randint
import calculator_area_vol as calc
from time import sleep
import sys

#   Code
exitChoice = ""
units = ['mm', 'cm', 'm', 'km']
valInp = ['a', 'area', 'v', 'volume']

while exitChoice.upper() != "EXIT":
    inp = input("Area or Volume(a or v) a/v: ")
    if inp.lower() not in valInp:
        print("You have not entered a valid input")
        calc

    if inp.lower() == "v" or inp.lower() == "volume":
        # Volume calculation

        l = input("Length: ")
        w = input("Width: ")
        h = input("Height: ")
        try:
            int(w)
            int(h)
            int(l)
        except:
            print("You have not entered a valid number")
            calc

        unit = input("Unit of mesurement: ")
        if unit.lower() not in units:
            print(f"Entered unit is not a real unit\nThe unit choices are {str(units)}")
            calc

        v = round(float(l)*float(h)*float(w), 2)

        try:
            if v == int(v):
                v = int(v)
            elif v != int(v):
                v = v
        except:
            v = v

        print("Volume\n")
        print(f" V = lwh\n V = {l}x{w}x{h}\n V = {v}{unit}^3\n")

        print("Capacity\n")

        if unit == "cm":
            c = float(v)
            cunit = "mL"
        elif unit == "mm":
            c = float(v/1000)
            cunit = "mL"
        elif unit == "m":
            c = float(v*1000)
            cunit = 'L'
        elif unit == "km":
            c = float(v*1000000)
            cunit = "ML"

        try:
            if c == int(c):
                c = int(c)
            elif c != int(c):
                c = float(c)
        except:
            c = c

        print(f" 1cm = 1mL\n 1m = 1000L\n C = {c}{cunit}")

    elif inp.lower() == "a" or inp.lower() == "area":
        # Area calculation
        l = input("Length: ")
        w = input("Width: ")
        try:
            int(l)
            int(w)
        except:
            print("You have not entered a valid number")
            calc

        unit = input("Unit of mesurement: ")
        if unit.lower() not in units:
            print(f"Entered unit is not a real unit\nThe unit choices are {str(units)}")
            calc

        a = round(float(l)*float(w), 2)

        try:
            if a == int(a):
                a = int(a)
            elif a != int(a):
                a = a
        except:
            a = a
        
        print("Area\n")
        print(f" A = lw \n A = {l}x{w}\n A = {a}{unit}^2") 

    exitChoice = input("Press return to play again, or type EXIT to leave: ")

exitConfirm = input("Please confirm your descision\nType abort to abort or do not type to continue: ")
if exitConfirm.lower() != "abort":
    print(".")
    sleep(randint(1, 3))
    print("..")
    sleep(randint(1, 2))
    print("...")
    sleep(randint(0, 2))
    print("Exiting")
    sleep(randint(0, 5))
    print("Exited")
    exit()
else:
    calc