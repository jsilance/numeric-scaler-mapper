import numpy as np
import cv2
import cvui
import json
import os
from gui_utils import *


WINDOW_NAME = 'CVUI Hello World!'

frame = np.zeros((400, 700, 3), np.uint8)

cvui.init(WINDOW_NAME)

id = [0]
x_in = [0]
y_in = [0]
x_size_in = [0]
y_size_in = [0]
r_in = [0]

x_out = [0]
y_out = [0]
x_size_out = [0]
y_size_out = [0]
r_out = [0]

col = [0]
lin = [0]

offset_x = [0]
offset_y = [0]

in_win = [0]
out_win = [0]



def json_converter(data):
	global id, x_in, y_in, x_size_in, y_size_in, r_in, x_out, y_out, x_size_out, y_size_out, r_out, col, lin, offset_x, offset_y, in_win, out_win

	json_updator(data, "offset_x", offset_x)
	json_updator(data, "offset_y", offset_y)
	json_updator(data, "col", col)
	json_updator(data, "row", lin)
	json_updator(data, "hide_input", in_win)
	json_updator(data, "hide_output", out_win)

	json_module_updator(data, id, "in_pos_x", x_in)
	json_module_updator(data, id, "in_pos_y", y_in)
	json_module_updator(data, id, "in_size_x", x_size_in)
	json_module_updator(data, id, "in_size_y", y_size_in)
	json_module_updator(data, id, "in_rotation", r_in)
	json_module_updator(data, id, "in_endpoint_x", x_in + x_size_in)
	json_module_updator(data, id, "in_endpoint_y", y_in + y_size_in)

	json_module_updator(data, id, "out_pos_x", x_out)
	json_module_updator(data, id, "out_pos_y", y_out)
	json_module_updator(data, id, "out_size_x", x_size_out)
	json_module_updator(data, id, "out_size_y", y_size_out)
	json_module_updator(data, id, "out_rotation", r_out)
	json_module_updator(data, id, "out_endpoint_x", x_out + x_size_out)
	json_module_updator(data, id, "out_endpoint_y", y_out + y_size_out)

	return data

def json_init_data(offset_x, offset_y, column, row):
	data = {}
	data["offset_x"] = offset_x
	data["offset_y"] = offset_y
	data["col"] = column
	data["row"] = row
	data["hide_input"] = True
	data["hide_output"] = True
	data["modules"] = {}
	return data

def json_loader(data):
	global id, x_in, y_in, x_size_in, y_size_in, r_in, x_out, y_out, x_size_out, y_size_out, r_out, col, lin, offset_x, offset_y
	pass

mod = []

if not os.path.exists("config.json"):
	json_object(json_init_data(0, 0, 1, 1))
	with open('config.json') as json_file:
		data = json.load(json_file)
else:
	with open('config.json') as json_file:
		data = json.load(json_file)
	mod, offset_x, offset_y, col, lin = json_to_gui_mod(data)


while True:
	frame[:] = (49, 52, 49)

	if len(mod) -1 < id[0]:
		mod.append(Gui_mod(0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


# -------------------------INPUT------------------------------

	cvui.text(frame, 40, 55, 'Module input')
	
	cvui.text(frame, 10, 85, 'X Position:')
	x_in[0] = mod[id[0]].pos_x
	cvui.counter(frame, 90, 80, x_in)
	if (x_in[0] < 0):
		x_in[0] = 0
	mod[id[0]].pos_x = x_in[0]

	cvui.text(frame, 10, 115, 'Y Position:')
	y_in[0] = mod[id[0]].pos_y
	cvui.counter(frame, 90, 110, y_in)
	if (y_in[0] < 0):
		y_in[0] = 0
	mod[id[0]].pos_y = y_in[0]

	cvui.text(frame, 10, 145, 'X Size:')
	x_size_in[0] = mod[id[0]].size_x
	cvui.counter(frame, 90, 140, x_size_in)
	if (x_size_in[0] < 0):
		x_size_in[0] = 0
	mod[id[0]].size_x = x_size_in[0]

	cvui.text(frame, 10, 175, 'Y Size:')
	y_size_in[0] = mod[id[0]].size_y
	cvui.counter(frame, 90, 170, y_size_in)
	if (y_size_in[0] < 0):
		y_size_in[0] = 0
	mod[id[0]].size_y = y_size_in[0]

	cvui.text(frame, 10, 205, 'Rotation:')
	r_in[0] = mod[id[0]].rot
	cvui.counter(frame, 90, 200, r_in, 90)
	if (r_in[0] < 0):
		r_in[0] = 270
	r_in[0] %= 360
	mod[id[0]].rot = r_in[0]

# ----------------------OUTPUT-----------------------------

	cvui.text(frame, 240, 55, 'Module output')

	cvui.text(frame, 210, 85, 'X Position:')
	x_out[0] = mod[id[0]].out_pos_x
	cvui.counter(frame, 290, 80, x_out)
	if (x_out[0] < 0):
		x_out[0] = 0
	mod[id[0]].out_pos_x = x_out[0]

	cvui.text(frame, 210, 115, 'Y Position:')
	y_out[0] = mod[id[0]].out_pos_y
	cvui.counter(frame, 290, 110, y_out)
	if (y_out[0] < 0):
		y_out[0] = 0
	mod[id[0]].out_pos_y = y_out[0]

	cvui.text(frame, 210, 145, 'X Size:')
	x_size_out[0] = mod[id[0]].out_size_x
	cvui.counter(frame, 290, 140, x_size_out)
	if (x_size_out[0] < 0):
		x_size_out[0] = 0
	mod[id[0]].out_size_x = x_size_out[0]

	cvui.text(frame, 210, 175, 'Y Size:')
	y_size_out[0] = mod[id[0]].out_size_y
	cvui.counter(frame, 290, 170, y_size_out)
	if (y_size_out[0] < 0):
		y_size_out[0] = 0
	mod[id[0]].out_size_y = y_size_out[0]

	cvui.text(frame, 210, 205, 'Rotation:')
	r_out[0] = mod[id[0]].out_rot
	cvui.counter(frame, 290, 200, r_out, 90)
	if (r_out[0] < 0):
		r_out[0] = 270
	r_out[0] %= 360
	mod[id[0]].out_rot = r_out[0]


# -----------------------AUTRES--------------------

	cvui.text(frame, 555, 15, 'Col:')
	cvui.counter(frame, 590, 10, col)
	if (col[0] < 1):
		col[0] = 1

	cvui.text(frame, 555, 45, 'Row:')
	cvui.counter(frame, 590, 40, lin)
	if (lin[0] < 1):
		lin[0] = 1

	cvui.text(frame, 460, 85, 'X Offset:')
	cvui.counter(frame, 540, 80, offset_x)
	if (offset_x[0] < 0):
		offset_x[0] = 0
	
	cvui.text(frame, 460, 115, 'Y Offset:')
	cvui.counter(frame, 540, 110, offset_y)
	if (offset_y[0] < 0):
		offset_y[0] = 0

	if cvui.button(frame, 500, 340, "Reset configuration"):
		os.remove("config.json")
		break

	cvui.checkbox(frame, 460, 150, 'Hide Input Window', in_win)

	cvui.checkbox(frame, 460, 180, 'Hide Output Window', out_win)
	
	cvui.text(frame, 10, 10, 'Box id:')
	id[0] += 1
	cvui.counter(frame, 60, 5, id)
	id[0] -= 1
	if (id[0] < 0):
		id[0] = 0
	elif (id[0] > (col[0] * lin[0]) - 1):
		id[0] -= 1
	elif len(mod) > (col[0] * lin[0]):
		mod.pop()

# -------------------------------------------------

	cvui.update()
	cvui.imshow(WINDOW_NAME, frame)

	# json_converter(data)
	json_object(json_converter(data))

	if cv2.waitKey(20) == 27 or not cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE):
		break