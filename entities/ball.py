# STDLIB
import math
import random
import itertools
import sys
import thread
import time

from lib.common import *
from lib.shape import *
from entity import *

class Ball(Entity):

	def __init__(self, x=0, y=0, r=CMAX, g=CMAX, b=CMAX, radius=8200):

		super(Ball, self).__init__(x, y, r, g, b)

		self.drawn = False
		self.pauseFirst = True
		self.pauseLast = True

		self.x = x
		self.y = y

		self.r = r
		self.g = g
		self.b = b

		self.radius = radius

		self._recalcBoundBox()

		self.samplePts = 100
		self.sampleCompensate = 100

	def setRadius(self, radius):
		self.radius = radius
		self._recalcBoundBox()

	def _recalcBoundBox(self):
		"""
		Call whenever size is reset to maintain an accurate
		bounding box. Note: Width and height are around a
		center coordinate: (x,y) = (0,0)
		"""
		# Bounding box calculation
		# Bottom should be negative of relative (0, 0) coord!
		self.top = self.radius
		self.bottom = -self.radius
		self.left = self.radius # TODO/FIXME: Correct?
		self.right = -self.radius # TODO/FIXME: Correct?

	def produce(self):
		"""
		Generate the points of the circle.
		"""
		r, g, b = (self.r, self.g, self.b)

		rad = self.radius
		pts = []

		for i in xrange(0, self.samplePts, 1):
			i = float(i) / self.samplePts * 2 * math.pi
			x = int(math.cos(i) * rad) + self.x
			y = int(math.sin(i) * rad) + self.y
			pt = (x, y, r, g, b)
			pts.append(pt)
			yield pt

		# XXX: Make sure galvos don't fall short.
		for i in xrange(0, self.sampleCompensate):
			yield pts[i]

		self.drawn = True

