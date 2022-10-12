from microbit import *
import music

back = False
front = False
backTriggerPoint = 600 # Must be positive number
frontTriggerPoint = -500 # Must be negative number

def alarm():
    display.show(Image('99999:'
                       '99999:'
                       '99999:'
                       '99999:'
                       '99999'))
    music.play(['f#'])

def batteryCheck():
    display.show(Image('90909:'
                       '09090:'
                       '90909:'
                       '09090:'
                       '90909'))
    sleep(200)
    display.clear()



while True:
    z_strength = accelerometer.get_z()

    if button_a.was_pressed():
        batteryCheck()
    if button_b.was_pressed():
        batteryCheck()
    
    if z_strength > backTriggerPoint:
        back = True
    else:
        back = False
    if z_strength < frontTriggerPoint:
        front = True
    else:
        front = False

    if front == True:
        alarm()
    else:
        if back == True:
            alarm()
        else:
            display.clear()
    
    sleep(100)
    
