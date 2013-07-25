import math

class Surface(object):

	def __init__(self, maxX, minX, maxY, minY):

		self.xMax = maxX
		self.xMin = minX
		self.yMax = maxY
		self.yMin = minY

		print self.xMax, self.xMin, self.yMax, self.yMin

		self.width = abs(maxX - minX)
		self.height = abs(maxY - minY)

		self.center = {
			'x': (maxX + minX)/2,
			'y': (maxY + minY)/2,
		}

		self.ratioFloat = self.width / (self.height*1.0)
		self.ratio = int(round(self.ratioFloat))

		self.rows = 0
		self.cols = 0
		self.cellWidth = 0 # width/cols
		self.cellHeight = 0 # height/rows

	def getArea(self):
		return self.width * self.height

	def getCenter(self):
		return self.center

	def inCell(self, x, y=None):
		if type(x) == dict and 'x' in x:
			x = x['x']
			y = x['y']

		if x < self.xMin or x > self.xMax or \
			y < self.yMin or y > self.yMax:
				return -1

		col = (x - self.xMin) / (self.width*1.0) * self.cols
		row = (y - self.yMin) / (self.height*1.0) * self.rows

		col = int(math.floor(col))
		row = int(math.floor(row))

		cell = (row * self.cols) + col

		return cell

	#
	# See if an object is outside of the bounding box
	#

	def isAbove(self, y, obj):
		return y + obj.top > self.yMax

	def isBelow(self, y, obj):
		return y + obj.bottom < self.yMin

	def isLeft(self, x, obj):
		return x + obj.left > self.xMax

	def isRight(self, x, obj):
		return x + obj.right < self.xMin


	#
	# Calculate the extremest coordinate that an object can be.
	#

	def topMost(self, obj):
		return self.yMax - obj.top

	def bottomMost(self, obj):
		return self.yMin - obj.bottom

	def leftMost(self, obj):
		return self.xMax - obj.left

	def rightMost(self, obj):
		return self.xMin - obj.right


