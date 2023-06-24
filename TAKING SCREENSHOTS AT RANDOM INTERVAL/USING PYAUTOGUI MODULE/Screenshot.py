from pyautogui import screenshot
from time import sleep
from random import randint

i = 1

while(True):
	ss = screenshot()
	ss.save("screenshot" + str(i) + ".png")

	i += 1
	
	print("screenshot Saved")
	sleep(randint(1,10)) # random from 1 to 10 seconds 