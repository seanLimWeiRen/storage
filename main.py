from microbit import *
import music

back = False
front = False

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
    
    if z_strength > 500:
        back = True
    else:
        back = False
    if z_strength < -500:
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
    
