#!/usr/bin/env python

"""
Laser Pong
Copyright 2013 Brandon Thomas <bt@brand.io>
See more laser-related projects at http://brand.io.
"""

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
from game_thread import *
from controller_thread import *
from controller import *
from configs import *
from surface import *

# PONG ENTITIES
from entities.box import *
from entities.wall import *
from entities.quad import *
from entities.ball import *
from entities.paddle import *

############################
#  OBJECT AND GAME SETUP
############################

surf = Surface(X_MAX, X_MIN, Y_MAX, Y_MIN)

ps = PointStream()
ps.setCenter(surf.absCenter['x'], surf.absCenter['y'])
ps.flipX = FLIP_X
ps.flipY = FLIP_Y
ps.showBlanking = False
ps.showTracking = False
ps.trackingSamplePts = 15
ps.blankingSamplePts = 15

ballRadius = (math.sqrt(surf.getArea()) / 20) * BALL_RADIUS_MULT
ball = Ball()
ball.setRadius(ballRadius)
ball.setPos(0, 0)
ball.setColor(0, CMAX, 0)

paddles = []
for i in range(2):
	paddle = Paddle()
	paddles.append(paddle)
	w = (surf.width * 1/64.0) * PADDLE_WIDTH_MULT # TODO: sqrt
	h = (surf.height * 1/3.0) * PADDLE_HEIGHT_MULT # TODO: sqrt
	paddle.setSize(w, h)

paddles[0].x = surf.left + paddles[0].width*2 + ballRadius
paddles[1].x = surf.right - paddles[0].width*2 - ballRadius

ps.objects.append(ball)
ps.objects.append(paddles[0])
ps.objects.append(paddles[1])

if DRAW_WALLS:
	walls = []
	for i in range(2):
		wall = Wall(length=surf.width)
		walls.append(wall)

	walls[0].y = surf.top
	walls[1].y = surf.bottom

	ps.objects.append(walls[0])
	ps.objects.append(walls[1])

if DRAW_SURFACE_BOX:
	box = Quad()
	box.setSize(surf.width, surf.height)
	box.edgeSamplePts = 40
	box.vertSamplePts = 10
	box.setColor(0, 0, CMAX)

	ps.objects.append(box)

def dac_thread():
	"""Pretty boring... Standard DAC thread."""
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

# GO, GO, GO!!!
# Note to non-Pythonistas: These *aren't* real hardware threads.
thread.start_new_thread(dac_thread, ())
thread.start_new_thread(game_thread, (surf, ball, paddles))
thread.start_new_thread(controller_thread, (surf, paddles))

while True:
	time.sleep(20000000)

