# STDLIB
import math
import random
import itertools
import sys
import thread
import time

from lib.common import *

from entity import *

class Wall(Entity):

	def __init__(self, x=0, y=0, r=CMAX, g=CMAX, b=CMAX, length=8000):

		super(Wall, self).__init__(x, y, r, g, b)

		self.drawn = False
		self.pauseFirst = True
		self.pauseLast = True

		self.length = length

		self.edgeSamplePts = 10
		self.vertSamplePts = 10

	def produce(self):
		"""
		Generate the points of the circle.
		"""
		r, g, b = (self.r, self.g, self.b)

		# Generate points
		ed = self.length/2

		pts = []
		pts.append({'x': ed, 'y': 0})
		pts.append({'x': -ed, 'y': 0})

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
				# XXX: FIX COLORS
				line.append((x, y, r, g, b))
			return line

		# DRAW THE SHAPE

		p = None # Save in scope

		for p in make_line(pts[0], pts[1], self.edgeSamplePts):
			break

		for i in range(self.vertSamplePts):
			yield p

		for p in make_line(pts[0], pts[1], self.edgeSamplePts):
			yield p

		for i in range(self.vertSamplePts):
			yield p

		self.lastPt = p
		self.drawn = True

