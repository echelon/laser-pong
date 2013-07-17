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
from controller import *
from configs import *
from surface import *

# Entities
from entities.box import *
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

paddles = []
for i in range(2):
	paddle = Paddle()
	paddles.append(paddle)
	w = surf.width * 1/64.0
	h = surf.height * 1/5.0
	paddle.setSize(w, h)

paddles[0].x = surf.xMax - paddles[0].width*2
paddles[1].x = surf.xMin + paddles[0].width*2

#paddles.append(Paddle())
#paddles.append(Paddle())
ball = Ball()
box = Quad()

box.setSize(surf.width, surf.height)
box.edgeSamplePts = 40
box.vertSamplePts = 10
box.r = CMAX
box.g = CMAX
box.b = CMAX

"""
grid = []
grid.append(Box())
grid[0].width = surf.cellWidth
grid[0].height = surf.cellHeight
grid[0].edgeSamplePts = 20
grid[0].vertSamplePts = 10
"""

ball.setRadius(1000)
ball.setPos(surf.getCenter())

ps.objects.append(paddles[0])
ps.objects.append(paddles[1])
ps.objects.append(ball)
ps.objects.append(box)
#ps.objects.append(grid[0])

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
	global ball
	global surf
	#global grid


	VEL_MIN = 500
	VEL_MAX = 1200

	ball.xVel = random.randint(VEL_MIN, VEL_MAX)
	ball.yVel = random.randint(VEL_MIN, VEL_MAX)

	while True:
		y = ball.y
		yVel = ball.yVel
		x = ball.x
		xVel = ball.xVel

		y += yVel
		x += xVel

		if surf.isAbove(y, ball):
			y = surf.topMost(ball)
			yVel = random.randint(VEL_MIN, VEL_MAX) * -1

		elif surf.isBelow(y, ball):
			y = surf.bottomMost(ball)
			yVel = random.randint(VEL_MIN, VEL_MAX)

		if surf.isLeft(x, ball):
			x = surf.leftMost(ball)
			xVel = random.randint(VEL_MIN, VEL_MAX) * -1

		elif surf.isRight(x, ball):
			x = surf.rightMost(ball)
			xVel = random.randint(VEL_MIN, VEL_MAX)


		for paddle in paddles:
			pass

		#print x, y, "grid",  surf.inCell(x, y)
		#coord = surf.getGridCenter(surf.inCell(x, y))
		#cell = surf.inCell(x, y)
		#grid[0].x = coord[0]
		#grid[0].y = coord[1]

		#print "cell", cell

		ball.y = y
		ball.yVel = yVel
		ball.x = x
		ball.xVel = xVel

		time.sleep(0.02) # Keep this thread from hogging CPU

def controller_thread():
	pygame.joystick.init()
	pygame.display.init()

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

			y += vert * 3000

			if surf.isAbove(y, paddle):
				y = surf.topMost(paddle)
			elif surf.isBelow(y, paddle):
				y = surf.bottomMost(paddle)

			paddle.y = y


		time.sleep(0.02) # Keep this thread from hogging CPU


thread.start_new_thread(dac_thread, ())
thread.start_new_thread(game_thread, ())
thread.start_new_thread(controller_thread, ())

"""
UNUSED STUFF
"""

while True:
	time.sleep(20000000)

