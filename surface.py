
class Surface(object):
	"""
	Input the raw, physical edges and generate a virtual playfield.
	The virtual field has a width, height, top, bottom, left, and right
	centered about (0, 0).

	PointStream handles the playfield translation about Surface.absCenter.
	"""

	def __init__(self, maxX, minX, maxY, minY):

		# XXX: Do not use these raw coordinates for math!
		# PointStream will be offset by Surface's `self.center` as a global 
		# correction. All objects use local (0, 0) map coordinates!
		self._xMax = maxX
		self._xMin = minX
		self._yMax = maxY
		self._yMin = minY

		# XXX: This is a physical center!
		# Everything below this assumes (0, 0).
		self.absCenter = {
			'x': (maxX + minX)/2,
			'y': (maxY + minY)/2,
		}

		self.width = abs(maxX - minX)
		self.height = abs(maxY - minY)

		hh, hw = (self.height/2, self.width/2)

		self.top = hh
		self.bottom = -hh
		self.left = -hw
		self.right = hw

	def getArea(self):
		return self.width * self.height

	def getAbsCenter(self):
		return self.absCenter

	#
	# See if an object is outside of the bounding box
	#

	def isAbove(self, y, obj):
		return y + obj.top > self.top

	def isBelow(self, y, obj):
		return y + obj.bottom < self.bottom

	def isLeft(self, x, obj):
		return x + obj.left < self.left

	def isRight(self, x, obj):
		return x + obj.right > self.right

	#
	# Calculate the extremest coordinate that an object can be.
	#

	def topMost(self, obj):
		return self.top - obj.top

	def bottomMost(self, obj):
		return self.bottom - obj.bottom

	def leftMost(self, obj):
		return self.left - obj.left

	def rightMost(self, obj):
		return self.right - obj.right


