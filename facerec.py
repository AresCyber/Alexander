import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
from time import sleep



def start_fr():
	count = 0
	countf = 0
	with open('labels', 'rb') as f:
		dicti = pickle.load(f)
		f.close()

	camera = PiCamera()
	camera.resolution = (640, 480)
	camera.framerate = 30
	rawCapture = PiRGBArray(camera, size=(640, 480))


	faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read("trainer.yml")

	font = cv2.FONT_HERSHEY_SIMPLEX

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		frame = frame.array
		frame = cv2.flip(frame, -1)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
		for (x, y, w, h) in faces:
			roiGray = gray[y:y+h, x:x+w]

			id_, conf = recognizer.predict(roiGray)

			for name, value in dicti.items():
				if value == id_:
					print(name)

			if conf <= 70:
				print("Face Recognized at Confidence Level" + str(conf) )
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)            
				count += 1
				if count == 10: 
					cv2.destroyAllWindows()
					camera.close()
					return 1
			else: 
				countf +=1

		if countf >= 30:
			cv2.destroyAllWindows()
			return 0
		else:
			print("countf is at " + str(countf))

		cv2.imshow('frame', frame)
		key = cv2.waitKey(1)

		rawCapture.truncate(0)

		if key == 27:
			break

	cv2.destroyAllWindows()
