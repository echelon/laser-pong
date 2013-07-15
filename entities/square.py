# STDLIB
import math
import random
import itertools
import sys
import thread
import time

from lib.shape import *
from lib.common import *

SQUARE_R = CMAX
SQUARE_G = CMAX
SQUARE_B = CMAX

SQUARE_EDGE_SAMPLE_PTS = 50
SQUARE_VERTEX_SAMPLE_PTS = 10

class Square(Shape):

	def __init__(self, x = 0, y = 0,
			r = 0, g = 0, b = 0,
			radius = 8200):

		super(Square, self).__init__(x, y, r, g, b)

		self.drawn = False
		self.pauseFirst = True
		self.pauseLast = True

		self.x = 0
		self.y = 0

		self.theta = 0
		self.thetaRate = 0

		self.radius = 10000

	def produce(self):
		"""
		Generate the points of the circle.
		"""
		r, g, b = (0, 0, 0)

		# Generate points
		ed = self.radius

		pts = []
		pts.append({'x': ed, 'y': ed})
		pts.append({'x': -ed, 'y': ed})
		pts.append({'x': -ed, 'y': -ed})
		pts.append({'x': ed, 'y': -ed})

		# Rotate points
		for p in pts:
			x = p['x']
			y = p['y']
			p['x'] = x*math.cos(self.theta) \
					- y*math.sin(self.theta)
			p['y'] = y*math.cos(self.theta) \
					+ x*math.sin(self.theta)

		# Translate points
		for pt in pts:
			pt['x'] += self.x
			pt['y'] += self.y

		r = CMAX
		g = CMAX
		b = CMAX

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

		for p in make_line(pts[0], pts[1],
				SQUARE_EDGE_SAMPLE_PTS):
			break
		for i in range(int(round(
				SQUARE_VERTEX_SAMPLE_PTS/2.0))):
			yield p
		for p in make_line(pts[0], pts[1],
				SQUARE_EDGE_SAMPLE_PTS):
			yield p
		for i in range(SQUARE_VERTEX_SAMPLE_PTS):
			yield p
		for p in make_line(pts[1], pts[2],
				SQUARE_EDGE_SAMPLE_PTS):
			yield p
		for i in range(SQUARE_VERTEX_SAMPLE_PTS):
			yield p
		for p in make_line(pts[2], pts[3],
				SQUARE_EDGE_SAMPLE_PTS):
			yield p
		for i in range(SQUARE_VERTEX_SAMPLE_PTS):
			yield p
		for p in make_line(pts[3], pts[0],
				SQUARE_EDGE_SAMPLE_PTS):
			self.lastPt = p # KEEP BOTH
			yield p
		for i in range(int(round(
				SQUARE_VERTEX_SAMPLE_PTS/2.0))):
			self.lastPt = p # KEEP BOTH
			yield p

		self.drawn = True


