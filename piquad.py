# Advancded mode for RPi quadcopter
# Very sensitive!!

# -*- coding: utf-8 -*-
from motor import motor
import direct_in
import RPi.GPIO as GPIO
import sys, tty, time, termios
from getch import getch

#Set up GPIO pins
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)


#Define getch() for live input/non-blocking input
"""def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(termios.TCSADRAIN, old_settings, fd)
    return ch"""

#Set up motors: l=left r=right b=back f=front
#where 17 is  GPIO17 = pin 11
lfmotor = motor('m1', 17, simulation=False)
rfmotor = motor('m1', 6, simulation=False)
lbmotor = motor('m1', 5, simulation=False) #17 may be faulty, switch with GPIO22, if needed
rbmotor = motor('m1', 4, simulation=False) #May need to switch mymotor with rbmotor etc


#Code start
#ESC already connected for Raspeberry Pi power
print('***Disconnect ESC power')
print('***then press ENTER')
get = raw_input()
lfmotor.start()
rfmotor.start()
lbmotor.start()
rbmotor.start()
lfmotor.setW(100)
rfmotor.setW(100)
lbmotor.setW(100)
rbmotor.setW(100)


#NOTE:the angular motor speed W can vary from 0 (min) to 100 (max)
#the scaling to pwm is done inside motor class
#Motor has already given start beeps, continue forward
print('***Connect ESC Power')
print('***Wait beep-beep')
print('***then press ENTER')
get = raw_input()
lfmotor.setW(0)
rfmotor.setW(0)
lbmotor.setW(0)
rbmotor.setW(0)

#Motor will fully intitialize on "beep"s
#PWM will be working fully
print('***Wait N beep for battery cell')
print('***Wait beep for ready')
print('***then press ENTER')
get = raw_input()

motortest = raw_input("Press return key to perform motor test: ")

#Start motor test
lfmotor.setW(10)
time.sleep(1)
lfmotor.setW(0)
time.sleep(0.25)
rfmotor.setW(10)
time.sleep(1)
rfmotor.setW(0)
time.sleep(0.25)
lbmotor.setW(10)
time.sleep(1)
lbmotor.setW(0)
time.sleep(0.25)
rbmotor.setW(10)
time.sleep(1)
rbmotor.setW(0)
time.sleep(0.25)

#Display input controls
print ('increase > Spacebar | decrease > v | save Wh > n | set Wh > h| KILL SWITCH > k')
print ('forward > w | backwards > s | right > d | left > a')

cycling = True
#time.sleep() used to return back to even motor speeds
try:
    while cycling:
        res = getch()
        if res == 'w':
            direct_in.mv_fwd()
            
        if res == 's':
            direct_in.mv_bwd()
            
        if res == 'q':                  #Yaw/Spin right: Increase lf and rb, decrease rf and lb
            direct_in.sp_left()
            
        if res == 'e':                  #Yaw/Spin left: Increase rf and lb, decrease lf and rb
            direct_in.sp_right()
            
        if res == 'a':                  #Roll left: Increase motors right, decrease motors left
            direct_in.mv_left()
            
        if res == 'd':                  #Roll right: Increase motors left, decrease motors right
            direct_in.mv_right()
            
        if res == ' ':                  #Increase all motor speeds simultaneously
            lfmotor.increaseW2()
            rfmotor.increaseW2()
            lbmotor.increaseW2()
            rbmotor.increaseW2()
            print("Altitude Increasing")
        if res == 'v':                  #Decrease all motor speeds simultaneously
            lfmotor.decreaseW2()
            rfmotor.decreaseW2()
            lbmotor.decreaseW2()
            rbmotor.decreaseW2()
            print("Altitude Decreasing")
       # if res == 'n':
          #  mymotor.saveWh()
       # if res == 'h':
         #   mymotor.setWh()
        if res == 'k':                  #KILL SWITCH: Stops all motors immediately, exits program
            print("KILLING PROCESSES")
            rfmotor.stop()
            lfmotor.stop()
            rbmotor.stop()
            lbmotor.stop()
            GPIO.cleanup()
            print("PROCESSES KILLED")
            exit()
        if res == 'l':                  #Land: stop all motors, still in program
            lfmotor.getW()
            while lfmotor.getW()>0 and rfmotor.getW() >0 and lbmotor.getW()>0 and rbmotor.getW()>0:
                lfmotor.getW()
                lfmotor.decreaseW()
                rfmotor.decreaseW()
                lbmotor.decreaseW()
                rbmotor.decreaseW()
                time.sleep(0.7)
                print("Landing")
                
finally:
    #shut down cleanly
    rfmotor.stop()
    lfmotor.stop()
    rbmotor.stop()
    lbmotor.stop()
    GPIO.cleanup()
    print ("Done")


