import math

"""
Divide the play area defined in configs.py into a grid system.
There will either be a 4x4, 2x4, or 4x2 grid constructed.

	Coordinate System:

		0	1	2	3
		4	5	6	7
		8	9	10	11
		12	13	14	15

	Or, similarly:

		0	1
		2	3
		4	5
		6	7

	Or,

		0	1	2	3
		4	5	6	7


"""

class Surface(object):

	def __init__(self, maxX, minX, maxY, minY):

		self.xMax = maxX
		self.xMin = minX
		self.yMax = maxY
		self.yMin = minY

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

		self.setGrid(4, 4)

		if self.ratioFloat < 0.75:
			self.setGrid(rows=4, cols=2)

		elif self.ratioFloat > 1.25:
			self.setGrid(rows=2, cols=4)

	def setGrid(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.cellWidth = self.width / self.cols
		self.cellHeight = self.height / self.rows

	def getGridCenter(self, gridNum):
		row = gridNum / self.rows
		col = gridNum % self.cols

		#print gridNum, row, col

		x = (row * self.cellWidth) + self.xMin + self.cellWidth/2
		y = (col * self.cellHeight) + self.yMin + self.cellHeight/2

		return (x, y)


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


