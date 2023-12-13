

import os

def jp():
	os.system('adb shell screencap /data/local/tmp/screen-temp.png')
	os.system('adb pull /data/local/tmp/screen-temp.png z:/temp/screen-temp.png')
	os.system('adb shell input swipe 100 900 100 100 200')

def show():
	img=io.imread("z:/temp/screen-temp.png")
	io.imshow(img)
	io.show()


from skimage import io

jp()
show()



