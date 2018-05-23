from mote import Mote
from time import sleep
from gpiozero import LED
from gpiozero import Button
import rainbowhat as rh

red = LED(17)
mote = Mote()
defaultspeed = 0.1
speed = 0.1
status = "off"
score = 0

def ispressed():
	global score
	global speed
	global defaultspeed
	if status == "on":
    		print("won")
		score = score + 1
		speed = speed * 0.9
		print(speed)
		rh.display.clear()
		rh.display.print_str(str(score))
		rh.display.show()
	if status == "off":
		print("Looser")
		rh.lights.rgb(1,1,1)
		for x in range(7):
			rh.rainbow.set_pixel(x, 255, 0, 0, brightness=1.0)
			rh.rainbow.show()
		sleep(2)
		rh.lights.rgb(0,0,0)
		rh.rainbow.clear()
		rh.rainbow.show()
		score = 0
		speed = defaultspeed
		rh.display.clear()
                rh.display.print_str(str(score))
                rh.display.show()

button = Button(4)
button.when_pressed = ispressed

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)

mote.clear()
while True:
	for pixel in range(16):
        	mote.clear()
		mote.set_pixel(1, pixel, 255, 0, 0)
                mote.set_pixel(2, pixel, 255, 0, 0)
		sleep(speed)
		mote.show()
	mote.clear()
	mote.show()
	red.on()
	status = "on"
	sleep(speed*2)
	red.off()
	status = "off"

