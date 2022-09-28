from microbit import *
import music

back = False
front = False

def alarm():
    display.show(Image.HEART)
    music.play(['f#'])



while True:
    z_strength = accelerometer.get_z()
    
    if z_strength > 400:
        back = True
    else:
        back = False
    if z_strength < -400:
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
