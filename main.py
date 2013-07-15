#!/usr/bin/env python

# STDLIB
import math
import random
import itertools
import sys
import thread
import time
from datetime import datetime, timedelta

# PYGAME
import pygame

# LASER LIB 

from lib import dac
from lib.common import *
from lib.stream import PointStream
from lib.shape import Shape

# PONG CODES
#from controller import setup_controls
#from controller import *
from configs import *
from surface import *

# Entities
from box import *
from ball import *
from paddle import *

ps = PointStream()
ps.showBlanking = False
ps.showTracking = False
ps.trackingSamplePts = 15
ps.blankingSamplePts = 15

surf = Surface(X_MAX, X_MIN, Y_MAX, Y_MIN)

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
box = Box()
box.width = surf.width
box.height = surf.height

paddle1.x = -10000
paddle2.x = 10000
ball.setPos(surf.getCenter())

ps.objects.append(paddle1)
ps.objects.append(paddle2)
ps.objects.append(ball)
ps.objects.append(box)

surf.inCell(12000, 10000)

def dac_thread():
	global ps

	while True:
		try:
			d = dac.DAC(dac.find_first_dac())
			d.play_stream(ps)

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"
			pass

def game_thread():
	while True:
		time.sleep(0.2) # Keep this thread from hogging CPU

def controller_thread():
	while True:
		time.sleep(0.2) # Keep this thread from hogging CPU

thread.start_new_thread(dac_thread, ())
thread.start_new_thread(game_thread, ())
thread.start_new_thread(controller_thread, ())

"""
UNUSED STUFF
"""

while True:
	time.sleep(20000000)

