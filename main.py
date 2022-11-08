from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from obj import Module
import module_fct as modf
from imutils import build_montages
import time
import json


SCREEN_SIZE = (1920, 1080)

# -------------- Module --------------
rectMod = []
# module_size = (256, 128)
# output_mod_size = (128, 64)

capture_area = (0, 0, 1920, 1080)
# resizer l'image matrice x module_size

matrice_output = (1, 1)
hide_input = False
hide_output = False

z = 0

# ---------------------------------------------

offset_x = 0
offset_y = 0

# i = 0
# k = 0

module_size = (256, 128)



def json_mod_loader():
	global rectMod, matrice_output, hide_input, hide_output, offset_x, offset_y
	with open('config.json') as json_file:
		data = json.load(json_file)
	offset_x = modf.data_searcher(data, "offset_x")
	offset_y = modf.data_searcher(data, "offset_y")
	matrice_output = (modf.data_searcher(data, "col"), modf.data_searcher(data, "row"))
	hide_input = modf.data_searcher(data, "hide_input")
	hide_output = modf.data_searcher(data, "hide_output")

	data_mod = modf.data_searcher(data, "modules")
	for r in data_mod:
		rectMod.append(Module((data_mod[r]["in_pos_x"], data_mod[r]["in_pos_y"]), (data_mod[r]["in_size_x"], data_mod[r]["in_size_y"]), data_mod[r]["in_rotation"], (data_mod[r]["out_pos_x"], data_mod[r]["out_pos_y"]), (data_mod[r]["out_size_x"], data_mod[r]["out_size_y"]), data_mod[r]["out_rotation"]))

def img_input_calculator(img):
	img_in = np.array(img)
	img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
	for r in rectMod:
		img_in = cv2.rectangle(img_in, r.pos, r.endpoint, (127, 63, 63), 2)
	
	cv2.imshow('Secret Capture', img_in)

def img_output_calculator(img):
	global rectMod
	img_out_pre = []
	for mod in rectMod:
		img_out_pre.append(mod.out_image)
	img_out = build_montages(img_out_pre, rectMod[0].out_size, matrice_output)
	for mod in img_out:
		mod = cv2.copyMakeBorder(mod, 0, 0, 12, 0, cv2.BORDER_CONSTANT, None, value = 0)
		# mod = cv2.rectangle(mod, )
		cv2.imshow('Output', mod)
	cv2.moveWindow('Output', offset_x - 20, offset_y - 31)

def controls():
	global capture_area, rectMod, module_size, matrice_output
	key = cv2.waitKey(1)
	if key == 27:
		return 1
	if not hide_input:
		if not cv2.getWindowProperty("Secret Capture", cv2.WND_PROP_VISIBLE):
			return 1
	if not cv2.getWindowProperty("Output", cv2.WND_PROP_VISIBLE):
		return 1


def mod_aquire(img):
	global rectMod
	if not img:
		pass
	img_mod = np.array(img)
	img_mod = cv2.cvtColor(img_mod, cv2.COLOR_BGR2RGB)
	for mod in rectMod:
		mod.image = img_mod[mod.pos[1]:mod.endpoint[1], mod.pos[0]:mod.endpoint[0]]
		if mod.rot == 90:
			mod.image = cv2.rotate(mod.image, cv2.ROTATE_90_CLOCKWISE)
		elif mod.rot == 180:
			mod.image = cv2.rotate(mod.image, cv2.ROTATE_180)
		elif mod.rot == 270:
			mod.image = cv2.rotate(mod.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
		# mod.image = img_mod[mod.pos[0]:mod.endpoint[0], mod.pos[1]:mod.endpoint[1]]
		mod.scale()

while True:
	start_time = time.time()

	z %= 100000
	if z == 0:
		json_mod_loader()
	z += 1

	img = ImageGrab.grab(bbox=capture_area)

	if not hide_input:
		img_input_calculator(img)
	if len(rectMod):
		mod_aquire(img)
	else:
		i, k = 0, 0

	if len(rectMod):
		img_output_calculator(img)

	# cv2.setMouseCallback('Secret Capture', add_module)

	# --------------
	# if (len(rectMod) < matrice_output[0] * matrice_output[1]):
	# 		rectMod.append(Module((i, k), module_size, 0, output_mod_size))
	# --------------

	if controls():
		break

	# print("FPS: ", 1.0 / (time.time() - start_time))

cv2.destroyAllWindows()
