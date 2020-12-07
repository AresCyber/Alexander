import io
import os
import picamera
import time
from datetime import datetime
from PIL import Image

def motion():
	camera = picamera.PiCamera()

	difference = 20
	pixels = 100
	count = 0
	width = 1280
	height = 960

	def compare():
		camera.resolution = (100, 75)
		stream = io.BytesIO()
		camera.capture(stream, format = 'bmp')
		stream.seek(0)
		im = Image.open(stream)
		buffer = im.load()
		stream.close()
		return im, buffer
	def newimage(width, height):
		time = datetime.now()
		filename = 'motion-%04d%02d%02d-%02d%02d%02d.jpg' % (time.year, time.month,time.day, time.hour,time.minute, time.second)
		camera.resolution = (width, height)
		camera.capture(filename)
		print("Captured Intruder")
		return 1
	image1, buffer1 = compare()

	timestamp = time.time()

	while (True):
		image2, buffer2 = compare()

		changedpixels = 0
		for x in range(0, 100):
			for y in range(0, 75):
				pixdiff = abs(buffer1[x,y][1]- buffer2[x,y][1])
				if pixdiff > difference:		
					changedpixels += 1
		if changedpixels > pixels:
			timestamp = time.time()
			thing = newimage(width, height)
			if thing == 1:
				count +=1
			#if 5 motion events are detected, initiate system. 
			if count == 4: 
				camera.close()
				return 1
		image1 = image2
		buffer1 = buffer2