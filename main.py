import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from obj import Module
import module_fct as modf
from imutils import build_montages


SCREEN_SIZE = (1920, 1080)

# -------------- Module --------------
rectMod = []
module_size = (192, 108)
output_mod_size = (192, 108)

capture_area = (0, 0, 1920, 1080)

matrice_output = (10, 10)
# ---------------------------------------------

i = 0
k = 0


def add_module(event, x, y, flags, params):
	global module_size, output_mod_size
	if event == cv2.EVENT_LBUTTONDOWN:
		if (len(rectMod) < matrice_output[0] * matrice_output[1]):
			rectMod.append(Module((x, y), module_size, 0, output_mod_size))
			i = x
			k = y

def img_input_calculator(img):
	img_in = np.array(img)
	img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
	for r in rectMod:
		img_in = cv2.rectangle(img_in, r.pos, r.endpoint, (127, 63, 63), 2)
	
	cv2.imshow('Secret Capture', img_in)

def img_output_calculator(img):
	img_out_pre = []
	for mod in rectMod:
		img_out_pre.append(mod.out_image)
	img_out = build_montages(img_out_pre, rectMod[0].out_size, matrice_output)
	for mod in img_out:
		cv2.imshow('Output', mod)

def last_rect_pos():
	global i, k, rectMod, module_size
	if len(rectMod):
		i = rectMod[len(rectMod) - 1].pos[0] + module_size[0]
		k = rectMod[len(rectMod) - 1].pos[1]
		if i > SCREEN_SIZE[0] or i + capture_area[0] > SCREEN_SIZE[0] or (len(rectMod) % matrice_output[0] == 0 and len(rectMod) > 0):
			i = rectMod[0].pos[0]
			k += module_size[1]

def controls():
	global capture_area, rectMod, module_size, matrice_output
	if cv2.waitKey(10) == ord('+'):
		if (len(rectMod) < matrice_output[0] * matrice_output[1]):
			rectMod.append(Module((i, k), module_size, 0, output_mod_size))
	elif cv2.waitKey(10) == ord('-') and len(rectMod) > 0:
		rectMod.pop()
	elif cv2.waitKey(10) == ord('0') and len(rectMod) > 0:
		rectMod.clear()
	elif cv2.waitKey(10) == ord('q'):
		return 1
	elif cv2.waitKey(10) == ord('w'):
		rectMod[len(rectMod) - 1].up()
	elif cv2.waitKey(10) == ord('a'):
		rectMod[len(rectMod) - 1].left()
	elif cv2.waitKey(10) == ord('s'):
		rectMod[len(rectMod) - 1].down()
	elif cv2.waitKey(10) == ord('d'):
		rectMod[len(rectMod) - 1].right()


def mod_aquire(img):
	global rectMod
	if not img:
		pass
	img_mod = np.array(img)
	img_mod = cv2.cvtColor(img_mod, cv2.COLOR_BGR2RGB)
	for mod in rectMod:
		mod.image = img_mod[mod.pos[1]:mod.endpoint[1], mod.pos[0]:mod.endpoint[0]]
		# mod.image = img_mod[mod.pos[0]:mod.endpoint[0], mod.pos[1]:mod.endpoint[1]]
		mod.scale()

while True:

	last_rect_pos()

	# img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
	img = ImageGrab.grab(bbox=capture_area)
	# img_input_calculator(img)
	if len(rectMod):
		mod_aquire(img)
	else:
		i, k = 0, 0

	if len(rectMod):
		img_output_calculator(img)

	cv2.setMouseCallback('Secret Capture', add_module)

	# --------------
	if (len(rectMod) < matrice_output[0] * matrice_output[1]):
			rectMod.append(Module((i, k), module_size, 0, output_mod_size))
	# --------------

	if controls():
		break

cv2.destroyAllWindows()
