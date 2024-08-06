from glob import glob
import pygame
from math import floor


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
grey = (200, 200, 220)
dark_grey = (100, 100 ,100)
yellow = (255, 255, 0)
purple = (200, 0, 200)
blue = (50, 50, 200)

objectCreated = []

def resetObjets():
	for i in range(len(objectCreated)):
		obj = objectCreated[i]
		obj.reset()

def deleteAllObjects():
	global objectCreated
	for i in range(len(objectCreated)):
		obj = objectCreated[i]
		obj.delete()

	objectCreated = []

def refreshObjets(avatar_b, background):
	for i in range(len(objectCreated)):
		obj = objectCreated[i]
		# global object.now
		if obj.movement_x == 0 and obj.movement_y == 0:
			continue
		
		obj.add_now()
		
		[x, y] = getLocObjet(obj)
		# print(obj.now, x, y)
		display = showObject(x, y).set_size(obj.size, background).get_object()
		if avatar_b.colliderect(display):
			# now = datetime.now()
			# print(now.time(), "hit")
			return False
	return True
		
def getLocObjet(object):

	if object.movement_x == 0:
		x_s = 0
	else:
		x_s = (object.movement_x) / object.speed
	if object.movement_y == 0:
		y_s = 0
	else:
		y_s = (object.movement_y) / object.speed
		
	if object.now <= object.speed:
		return [object.x + x_s * object.now, object.y + y_s * object.now]

	else:
		return [(object.x + object.movement_x) + x_s * (object.speed - object.now), (object.y + object.movement_y) + y_s * (object.speed - object.now)]
		
class createObject:

	def __init__(self, x= 0, y=0):
		self.x = x
		self.y = y
		self.movement_x = 0
		self.movement_y = 0
		self.now = 0
		self.nowDefault = 0
		self.size = 3
		self.speed = 0
		self.Boomerang = True
		objectCreated.append(self)

	def set_size(self, size):
		self.size = size
		return self

	def set_speed(self, speed):
		self.speed = speed
		return self

	def set_movement(self, x, y):
		self.movement_x = x
		self.movement_y = y
		return self

	def reset(self):
		self.now = self.nowDefault
	def delete(self):
		del self
		
	def set_Boomerang(self, a):
		self.Boomerang = a
		return self

	def set_now(self, now):
		self.now = now
		self.nowDefault = now
		return self

	def add_now(self):
		self.now = self.now + 1
		if self.Boomerang == True:
			if self.now > self.speed * 2:
				self.now = self.now % (self.speed * 2)
		else:
			if self.now > self.speed:
				self.now = self.now % self.speed
		# self.now = self.now + 1
		# if self.Boomerang == True:
		# 	if self.now > self.speed * 2:
		# 		self.now = 0
		# else:
		# 	if self.now > self.speed:
		# 		self.now = 0


class showObject:

	def __init__(self, x= 0, y=0):
		self.locX = x
		self.locY = y
        # self.backGround = back

	def set_size(self, size, background):
		self.circle = pygame.draw.circle(background, blue, (self.locX, self.locY), size)
		self.circle_b = pygame.draw.circle(background, black, (self.locX, self.locY), size, floor(size/ 3))
		return self

	def get_object(self):
		return self.circle_b
