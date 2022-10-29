import numpy as np
import cv2
import cvui

WINDOW_NAME = 'CVUI Hello World!'

frame = np.zeros((200, 500, 3), np.uint8)

cvui.init(WINDOW_NAME)

id = [0]
x_in = [0]
y_in = [0]
r_in = [0]

x_out = [0]
y_out = [0]
r_out = [0]

col = [0]
lin = [0]

while True:
	frame[:] = (49, 52, 49)

	cvui.text(frame, 10, 10, 'Box id:')
	cvui.counter(frame, 60, 5, id)
	if (id[0] < 0):
		id[0] = 0

	cvui.text(frame, 40, 55, 'Module input')
	
	cvui.text(frame, 10, 85, 'X Position:')
	cvui.counter(frame, 90, 80, x_in)

	cvui.text(frame, 10, 115, 'Y Position:')
	cvui.counter(frame, 90, 110, y_in)

	cvui.text(frame, 10, 145, 'Rotation:')
	cvui.counter(frame, 90, 140, r_in)


	cvui.text(frame, 240, 55, 'Module output')

	cvui.text(frame, 210, 85, 'X Position:')
	cvui.counter(frame, 290, 80, x_out)

	cvui.text(frame, 210, 115, 'Y Position:')
	cvui.counter(frame, 290, 110, y_out)

	cvui.text(frame, 210, 145, 'Rotation:')
	cvui.counter(frame, 290, 140, r_out)



	cvui.text(frame, 355, 15, 'Col:')
	cvui.counter(frame, 390, 10, col)

	cvui.text(frame, 355, 45, 'Lin:')
	cvui.counter(frame, 390, 40, lin)



	cvui.imshow(WINDOW_NAME, frame)

	if cv2.waitKey(20) == 27:
		break