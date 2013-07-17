# STDLIB
import math
import random
import itertools
import sys
import thread
import time

from lib.shape import *
from lib.common import *

from quad import *

class Square(Quad):
	def __init__(self, x=0, y=0, r=CMAX, g=CMAX, b=CMAX, edge=2000):
		super(Square, self).__init__(x, y, r, g, b, width=edge, height=edge)

	def setSize(self, edge):
		super(Square, self).setSize(edge, edge)

