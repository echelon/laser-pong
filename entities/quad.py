from lib.common import *
from lib.shape import *
from entity import *

class Quad(Entity):

	def __init__(self, x=0, y=0, r=CMAX, g=CMAX, b=CMAX,
					width=1000, height=2000):

		super(Quad, self).__init__(x, y, r, g, b)

		self.x = x
		self.y = y

		self.r = r
		self.g = g
		self.b = b

		self.width = width
		self.height = height

		# Bounding box
		self.top = 0
		self.bottom = 0
		self.left = 0
		self.right = 0

		self._recalcBoundBox()

		self.edgeSamplePts = 10
		self.vertSamplePts = 10

		self.drawn = False
		self.pauseFirst = True
		self.pauseLast = True

	def setSize(self, width, height):
		self.width = width
		self.height = height
		self._recalcBoundBox()

	def produce(self):
		"""
		Generate the points of the circle.
		"""
		r, g, b = (self.r, self.g, self.b)

		w = self.width/2
		h = self.height/2

		pts = []
		pts.append({'x': w, 'y': h})
		pts.append({'x': w, 'y': -h})
		pts.append({'x': -w, 'y': -h})
		pts.append({'x': -w, 'y': h})

		# Translate points
		for pt in pts:
			pt['x'] += self.x
			pt['y'] += self.y

		def make_line(pt1, pt2, steps=200):
			xdiff = pt1['x'] - pt2['x']
			ydiff = pt1['y'] - pt2['y']
			line = []
			for i in xrange(0, steps, 1):
				j = float(i)/steps
				x = pt1['x'] - (xdiff * j)
				y = pt1['y'] - (ydiff * j)
				line.append((x, y, r, g, b))
			return line

		# ************** #
		# DRAW THE SHAPE #
		# ************** #

		p = None # Save in scope

		for p in make_line(pts[0], pts[1], self.edgeSamplePts):
			break

		for i in range(int(round(self.vertSamplePts/2.0))):
			yield p

		for p in make_line(pts[0], pts[1], self.edgeSamplePts):
			yield p

		for i in range(self.vertSamplePts):
			yield p

		for p in make_line(pts[1], pts[2], self.edgeSamplePts):
			yield p

		for i in range(self.vertSamplePts):
			yield p

		for p in make_line(pts[2], pts[3], self.edgeSamplePts):
			yield p

		for i in range(self.vertSamplePts):
			yield p

		for p in make_line(pts[3], pts[0], self.edgeSamplePts):
			self.lastPt = p # KEEP BOTH
			yield p

		for i in range(int(round(self.vertSamplePts/2.0))):
			self.lastPt = p # KEEP BOTH
			yield p

		self.drawn = True

