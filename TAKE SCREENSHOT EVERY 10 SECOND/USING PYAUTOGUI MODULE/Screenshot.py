from time import sleep
from pyautogui import screenshot

i = 1

while(True):
	ss = screenshot()
	ss.save("Screenshot" + str(i) + ".png")
	i += 1
	print("Screenshot Saved")
	sleep(10)