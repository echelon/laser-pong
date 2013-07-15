from lib.shape import *

class Entity(Shape):

	def __init__(self, x = 0, y = 0, r = 0, g = 0, b = 0):

		super(Entity, self).__init__(x, y, r, g, b)

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setPos(self, x, y=0):
		if type(x) == dict:
			self.x = x['x']
			self.y = x['y']
			return

		self.x = x
		self.y = y

	def checkCollide(self, other):
		"""
		Determine if two objects collide.
		"""
		rad = other.collisionRadius + self.collisionRadius
		hyp = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
		return (hyp < rad)

