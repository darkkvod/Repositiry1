import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt;
GPIO.setmode(GPIO.BCM)
ber=[10, 9 ,11 ,5,6 ,13 ,19, 26]
reb=[26,19,13,6,5,11,9,10]
for n in ber:
    GPIO.setup(n, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.OUT)


measure = []
T = []


def lightNumber(decNumber):
    n=[0,0,0,0,0,0,0,0]
    n=binc(decNumber)
    for i in range(8):
        GPIO.output(reb[i],n[i])

def binc(num):
    n=7
    p=0
    X=[]
    while n>0:
        p=int(num/2**n)
        if p== 1:
            X.append(1)
            num-=2**n
        else:
            X.append(0)
        n-=1
    X.append(num)
    return X

def lightNumber(decNumber):
    n=[0,0,0,0,0,0,0,0]
    n=binc(decNumber)
    for i in range(8):
        GPIO.output(reb[i],n[i])

def adc():
    x = 0
    y = 256
    while(y-x)>1:
        p = int((x+y)/2)
        lightNumber(p)
        time.sleep(0.01)
        if GPIO.input(4) == 0:
            y=p
        else:
            x = p
    time.sleep(0.01)
    return x

timeStart = time.time()

try:
    
    GPIO.output (17,1)
    a = adc()
    while( a < 250):
        a = adc()
        b = float(time.time()) - float(timeStart)
        T.append(b)
        measure.append(a)
        print( a  , "=" , (float(a)/255)*3.24, "V")  
    GPIO.output (17,0)
    a = adc()
    while( a > 1):
        a = adc()
        b = float(time.time()) - float(timeStart)
        T.append(b)
        measure.append(a)
        print( a  , "=" , (float(a)/255)*3.24, "V")  

    plt.plot(T, measure)
    plt.title( 'Voltage(Time)')
    plt.xlabel( 'Time' )
    plt.ylabel( 'Voltage' )
    plt.show()

    print(measure,"\n", T)
    
    
    
finally:
    for x in range (8):
        GPIO.output (reb[x],0)
GPIO.output (17,0)
GPIO.cleanup()