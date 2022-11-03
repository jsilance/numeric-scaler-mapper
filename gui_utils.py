import json 

class Gui_mod:
	def __init__(self, in_pos_x, in_pos_y, in_size_x, in_size_y, in_rot, out_pos_x, out_pos_y, out_size_x, out_size_y, out_rot):
		self.pos_x = in_pos_x
		self.pos_y = in_pos_y
		self.size_x = in_size_x
		self.size_y = in_size_y
		self.rot = in_rot
		self.endpoint_x = in_pos_x + in_size_x
		self.endpoint_y = in_pos_y + in_size_y

		self.out_pos_x = out_pos_x
		self.out_pos_y = out_pos_y
		self.out_size_x = out_size_x
		self.out_size_y = out_size_y
		self.out_rot = out_rot
		self.out_endpoint_x = out_pos_x + out_size_x
		self.out_endpoint_y = out_pos_y + out_size_y


def json_updator(data, param, value):
	data["{}".format(param)] = value[0]

def json_module_updator(data, id, param, value):
	if id[0] < 0:
		return
	if not "{}".format(id[0]) in data["modules"]: 
		data["modules"]["{}".format(id[0])] = {}
	data["modules"]["{}".format(id[0])]["{}".format(param)] = value[0]

def json_object(input):
	with open('config.json', 'w') as outfile:
		json.dump(input, outfile)

def json_to_gui_mod(data):
	off_x = []
	off_y = []
	columns = []
	rows = []

	off_x.append(data["offset_x"])
	off_y.append(data["offset_y"])
	columns.append(data["col"])
	rows.append(data["row"])
	mod = []
	for i in data["modules"]:
		mod.append(Gui_mod(data["modules"][i]["in_pos_x"], data["modules"][i]["in_pos_y"], data["modules"][i]["in_size_x"], data["modules"][i]["in_pos_y"], data["modules"][i]["in_rotation"], data["modules"][i]["out_pos_x"], data["modules"][i]["out_pos_y"], data["modules"][i]["out_size_x"], data["modules"][i]["out_pos_y"], data["modules"][i]["out_rotation"]))
	return mod, off_x, off_y, columns, rows