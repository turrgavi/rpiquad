from motor import motor
import RPi.GPIO as GPIO
import time

#Set up GPIO pins
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

#Set up motors: l=left r=right b=back f=front
#where 17 is  GPIO17 = pin 11
lfmotor = motor('m1', 17, simulation=False)
rfmotor = motor('m1', 6, simulation=False)
lbmotor = motor('m1', 5, simulation=False) #17 may be faulty, switch with GPIO22, if needed
rbmotor = motor('m1', 4, simulation=False) #May need to switch mymotor with rbmotor etc

def mv_fwd():
    lfmotor.decreaseW2()
    rfmotor.decreaseW2()
    lbmotor.increaseW2()
    rbmotor.increaseW2()
    time.sleep(0.1)
    lfmotor.increaseW2()
    rfmotor.increaseW2()
    lbmotor.decreaseW2()
    rbmotor.decreaseW2()
    print("Roll FORWARD")

def mv_bwd():
    lfmotor.increaseW2()
    rfmotor.increaseW2()
    lbmotor.decreaseW2()
    rbmotor.decreaseW2()
    time.sleep(0.1)
    lfmotor.decreaseW2()
    rfmotor.decreaseW2()
    lbmotor.increaseW2()
    rbmotor.increaseW2()
    print("Roll BACKWARDS")

def mv_left():
    lfmotor.decreaseW2()
    lbmotor.decreaseW2()
    rfmotor.increaseW2()
    rbmotor.increaseW2()
    time.sleep(0.1)             #Return motors back to even speed
    lfmotor.increaseW2()
    lbmotor.increaseW2()
    rfmotor.decreaseW2()
    rbmotor.decreaseW2()
    print("Roll LEFT")

def mv_right():
    rfmotor.decreaseW2()
    rbmotor.decreaseW2()
    lfmotor.increaseW2()
    lbmotor.increaseW2()
    time.sleep(0.1)             #Return motors back to even speed
    rfmotor.increaseW2()
    rbmotor.increaseW2()
    lfmotor.decreaseW2()
    lbmotor.decreaseW2()
    print("Roll RIGHT")

def sp_right():
    rfmotor.increaseW2()
    lbmotor.increaseW2()
    lfmotor.decreaseW2()
    rbmotor.decreaseW2()
    time.sleep(0.1)
    rfmotor.decreaseW2()
    lbmotor.decreaseW2()
    lfmotor.increaseW2()
    rbmotor.increaseW2()
    print("Yaw RIGHT")

def sp_left():
    lfmotor.increaseW2()
    rbmotor.increaseW2()
    rfmotor.decreaseW2()
    lbmotor.decreaseW2()
    time.sleep(0.1)
    lfmotor.decreaseW2()
    rbmotor.decreaseW2()
    rfmotor.increaseW2()
    lbmotor.increaseW2()
    print("Yaw LEFT")
