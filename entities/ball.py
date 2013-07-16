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

	def __init__(self, x = 0, y = 0, r = 0, g = 0, b = 0, radius = 8200):

		super(Ball, self).__init__(x, y, r, g, b)

		self.drawn = False
		self.pauseFirst = True
		self.pauseLast = True

		self.x = x
		self.y = y

		self.r = CMAX
		self.g = CMAX
		self.b = CMAX

		self.radius = radius

		# Bounding box calculation
		# Bottom should be negative of relative (0, 0) coord!
		self.top = radius
		self.bottom = -radius
		self.left = radius
		self.right = -radius

		self.samplePts = 100
		self.sampleCompensate = 100

	def setRadius(self, radius):
		"""
		Important to redefine bounding box.
		"""
		self.radius = radius
		self.top = radius
		self.bottom = -radius
		self.left = radius
		self.right = -radius

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
