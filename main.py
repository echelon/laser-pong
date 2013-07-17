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
from game_thread import *
from controller import *
from configs import *
from surface import *

# Entities
from entities.box import *
from entities.wall import *
from entities.quad import *
from entities.ball import *
from entities.paddle import *

############################
#  OBJECT AND GAME SETUP
############################

ps = PointStream()
ps.flipX = FLIP_X
ps.flipY = FLIP_Y
ps.showBlanking = False
ps.showTracking = False
ps.trackingSamplePts = 15
ps.blankingSamplePts = 15

surf = Surface(X_MAX, X_MIN, Y_MAX, Y_MIN)
ballRadius = surf.getArea() / 200000

paddles = []
for i in range(2):
	paddle = Paddle()
	paddles.append(paddle)
	w = surf.width * 1/64.0
	h = surf.height * 1/3.0
	paddle.setSize(w, h)

paddles[0].x = surf.xMax - paddles[0].width*2 - ballRadius
paddles[1].x = surf.xMin + paddles[0].width*2 + ballRadius

walls = []
for i in range(2):
	wall = Wall(length=surf.width)
	walls.append(wall)

walls[0].y = surf.yMax
walls[1].y = surf.yMin

ball = Ball()
ball.setRadius(ballRadius)
ball.setPos(surf.getCenter())

box = Quad()
box.setSize(surf.width, surf.height)
box.edgeSamplePts = 40
box.vertSamplePts = 10
box.r = CMAX
box.g = CMAX
box.b = CMAX

ps.objects.append(ball)
ps.objects.append(paddles[0])
ps.objects.append(paddles[1])

if DRAW_WALLS:
	ps.objects.append(walls[0])
	ps.objects.append(walls[1])

def controller_thread():
	pygame.joystick.init()
	pygame.display.init()

	PADDLE_VEL = surf.getArea() / 200000

	# Wait until we have a joystick
	# TODO: Doesn't account for unplugged. 
	while not pygame.joystick.get_count():
		print "No Joystick detected!"
		time.sleep(5)

	controls = []
	controls.append(init_controls(0))
	controls.append(init_controls(1))

	while True:
		e = pygame.event.get()

		lVert, lHori, rVert, rHori = (0, 0, 0, 0)

		for i in range(len(paddles)):

			paddle = paddles[i]
			control = controls[i]
			lVert = control.getLeftVert()
			rVert = control.getRightVert()

			vert = lVert or rVert
			y = paddle.y

			y += vert * PADDLE_VEL

			if surf.isAbove(y, paddle):
				y = surf.topMost(paddle)
			elif surf.isBelow(y, paddle):
				y = surf.bottomMost(paddle)

			paddle.y = y


		time.sleep(0.02) # Keep this thread from hogging CPU

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

"""
GO, GO, GO!!!
"""

thread.start_new_thread(dac_thread, ())
thread.start_new_thread(game_thread, (surf, ball, paddles))
thread.start_new_thread(controller_thread, ())

while True:
	time.sleep(20000000)

