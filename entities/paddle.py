from lib.common import *
from lib.shape import *
from lib.common import *

from quad import *

class Paddle(Quad):

	def __init__(self, x=0, y=0, r=CMAX, g=CMAX, b=CMAX,
					width=1000, height=2000):
		super(Paddle, self).__init__(x, y, r, g, b, width, height)
