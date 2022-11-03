import numpy as np
import cv2

class Module:
	def __init__(self, p_pos, p_size, p_rot, p_out_size):
		self.pos = p_pos
		self.size = p_size
		self.rot = p_rot
		self.endpoint = tuple(map(sum, zip(self.pos, self.size)))

		self.out_pos = (0, 0)
		self.out_size = p_out_size
		self.out_rot = 0
		self.out_endpoint = tuple(map(sum, zip(self.out_pos, self.out_size)))

		self.image = ""
		self.out_image = ""
	
	def scale(self):
		self.out_image = cv2.resize(self.image, self.out_size)

	def up(self):
		self.pos = (self.pos[0], self.pos[1] - 10)
		self.endpoint = (self.endpoint[0], self.endpoint[1] - 10)
	def left(self):
		self.pos = (self.pos[0] - 10, self.pos[1])
		self.endpoint = (self.endpoint[0] - 10, self.endpoint[1])
	def down(self):
		self.pos = (self.pos[0], self.pos[1] + 10)
		self.endpoint = (self.endpoint[0], self.endpoint[1] + 10)
	def right(self):
		self.pos = (self.pos[0] + 10, self.pos[1])
		self.endpoint = (self.endpoint[0] + 10, self.endpoint[1])

	def rotate_in(self):
		self.rot = self.rot % 360
		self.rot += 15
	def rotate_out(self):
		self.rot = self.rot % 360
		self.out_rot += 15
