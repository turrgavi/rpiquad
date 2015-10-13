import os, time
import RPi.GPIO as GPIO

gateway_ip = raw_input("Enter gateway ip: ")

hostname = gateway_ip #ip of server

response = os.system("ping -c 1 " + hostname)

try:

    if response == 0:
        print hostname, ' Connected'

    else:
        print hostname, ' is down'

    while True:
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            print ".",
            time.sleep(0.5)
        elif response != 0:
            print ("WARNING: DISCONNECTED\n\n\n")
            print ("Disabling...")
            GPIO.cleanup()
            print ("Disabled.")
            break

finally:
    print ("Complete, ping not running.")
