
HARDWARE_X_MAX = 33000
HARDWARE_X_MIN = 33000
HARDWARE_Y_MAX = 33000
HARDWARE_Y_MIN = 33000

class Surface(object):

	def __init__(self, maxX, minX, maxY, minY):
		self.maxX = maxX
		self.minX = minX
		self.maxY = maxY
		self.minY = minY

		self.width = abs(maxX - minX)
		self.height = abs(maxY - minY)

		self.center = {
			'x': (maxX + minX)/2,
			'y': (maxY + minY)/2,
		}

