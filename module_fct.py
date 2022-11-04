from obj import *
import cv2


def mouse_pos(event, x, y, flags, params):
	# if event == cv2.EVENT_LBUTTONDOWN:
	while event == cv2.EVENT_MOUSEMOVE:
		print(x, y)
		if event == cv2.EVENT_LBUTTONUP:
			break

def data_searcher(data, params):
	return data["{}".format(params)]
