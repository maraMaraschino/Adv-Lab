import serial
import time
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt
import pandas as pd
import math as m
import datetime

def degreeconvert(a,b):
    a = int(a)
    b = int(b)
    ba = '{:0>8}'.format(str(bin(a))[2:]) #display the strings passed as 8 bit binary
    bb = '{:0>8}'.format(str(bin(b))[2:])

    #this step was described in the SPI documentation for the Rotary Encoder
    total = ba[4:] + bb #combine the second half of the first byte with the second to get the data point

    number = int(total,2) #convert that binary number into a usable integer
    deg = (number * 360)/4096 #convert that integer into a value in degrees
    return deg

def pressureconvert(p,r):
    bp = '{:0>8}'.format(str(bin(p))[2:]) #converts the numbers passed in as 8 bit binary
    br = '{:0>8}'.format(str(bin(r))[2:])

    p1 = bp[2:] 

    ptotal = p1 + br #combine part of the first number with the second
    
    output = int(ptotal, 2) #convert the number to decimal form

    #below code converts the decimal number into a kPa pressure value
    #____________________________________________________________________#
    percent_output = (output/16384)*100 

    pressure = ((percent_output-10)*(1.6))/80
    pressurekpa = pressure*100
    #____________________________________________________________________#
    return pressurekpa

def tempconvert(o,t): #converts the hex value to a temperature reading
    bo = '{:0>8}'.format(str(bin(o))[2:])
    bt = '{:0>8}'.format(str(bin(t))[2:])
    
    z = bo + bt
    x = '0b' + z
    c = int(x,2)
    v = c>>2
    n = v*0.25
    return n


MYINITIALS = 'GAKWAF'

#Here is the filename construction based upon date and time.
ddtt = datetime.datetime.now()
nameformat="%Y%m%d_%H%M%S"
myrootfilename = MYINITIALS + ddtt.strftime(nameformat)

PORT = 'COM5' #change this to the port your arduino is connected to

tfile = "Data/" + myrootfilename + ".txt" #creates the full file name to save the raw data to
cfile = "Data/" + myrootfilename + ".csv" #creates the full file name to save the useable data to

num = ""
num = input("Enter Desired Number of Data Points: ") #prompts the user to input the number of data points to take

rawdata = []
arduino = serial.Serial(port=PORT,  baudrate=115200, timeout=.1) #connect to the Arduino
arduino.close()
#letter = "a" #uncomment for append
letter = "w" #uncomment for write over
file = open(tfile,letter)#creates or opens a file to save the data to

i = 0
while(i < int(num)):
    #print('inside first loop',i,'\n')

    #time.sleep(0.1) #wait for the arduino to collect the data
    while True:
        arduino.write(bytes("1\n",  'utf-8'))#writes the value x as a byte to the arduino
        l = arduino.read(1) #read one byte from the Arduino
        #print('read a byte from the Arduino', l)
        if(l == b'%'): #wait until the Arduino sends a %
            data = arduino.readline() #read the data in
            break
    rawdata.append(str(data)+"\n")
    i += 1

file.writelines(rawdata) #saves the data to a .txt file
print("Data Saved as", tfile)
file.close() #close connection to the file
arduino.close() #close connection to the arduino 
