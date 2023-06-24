import pyscreenshot
from time import sleep

i = 1
while(True):
	img = pyscreenshot.grab()

	img.save("ScreenShot" + str(i) + ".png")
	
	print("Screenshot Saved")
	i += 1;
	sleep(10)
	
