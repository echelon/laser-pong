from lib.shape import *
from lib.common import *

class Entity(Shape):

	def __init__(self, x=0, y=0, r=CMAX, g=CMAX, b=CMAX):

		super(Entity, self).__init__(x, y, r, g, b)

		self.xVel = 0
		self.yVel = 0

		# Bounding box calculation
		# Bottom should be negative of relative (0, 0) coord!
		self.top = 0
		self.bottom = 0
		self.left = 0
		self.right = 0

		self.collisionRadius = 0

	def _recalcBoundBox(self):
		"""
		Call whenever size is reset to maintain an accurate
		bounding box. Note: Width and height are around a
		center coordinate: (x,y) = (0,0)
		"""
		w = self.width/2
		h = self.height/2

		# Bounding box calculation
		# Bottom should be negative of relative (0, 0) coord!
		self.top = h
		self.bottom = -h
		self.left = w
		self.right = -w

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setPos(self, x, y=0):
		if type(x) == dict and 'x' in x:
			self.x = x['x']
			self.y = x['y']
			return

		self.x = x
		self.y = y

	#def checkCollide(self, other):
	#	"""
	#	Determine if two objects collide.
	#	"""
	#	rad = other.collisionRadius + self.collisionRadius
	#	hyp = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
	#	return (hyp < rad)

