# rpiquad
#Raspberry Pi quadcopter source code. Written in Python using standard RPi B+ GPIO pins.

This source code is written in Python v2, it uses 6 GPIO pins: GPIO17, GPIO6, GPIO5, and GPIO4. As well as 4 GND pins and 1 5v Pin.

This will require 4 escs, 4 brushless motors, a Rapsberry Pi B+, a LiPo battery(4200maH preffered), and a quadcopter frame.

Extras may include Dean's connector, gold plated pin connectors etc...

Features:
  -KILL SWITCH: Stops all motors, GPIO.cleanup(), program end.
  -Auto-land: Slowly lowers motor speeds equally
  
  *Soon to be added motor speed equalizer
  *Soon to be added live sensitivity adjustment
  *Soon to be added auto-takeoff
  *Soon to be added "Set hover"

There are 3 modes at which you can fly; Beginner, Modest, and Advancded.

Beginner:
  -Low sensitivity
  -Low climb and descent speeds [Intergrals of 1]
  
Modest:
  -Medium sensitivity
  -Medium climb and descent speeds [Intergrals of 2]
  
Advanced:
  -High sensitivity
  -High climb and descent speeds [Intergrals of 3]
  *Soon to be added live sensitivity adjustment
  *Soon to be added auto-takeoff
  *Soon to be added "Set hover feature"
