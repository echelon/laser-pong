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

		self.rows = 4
		self.cols = 4

		if self.ratioFloat < 0.75:
			self.rows = 4
			self.cols = 2

		elif self.ratioFloat > 1.25:
			self.rows = 2
			self.cols = 4

		self.cellWidth = self.width / self.cols
		self.cellHeight = self.height / self.rows

		print self.width, self.height
		print self.cellWidth, self.cellHeight

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

