# STDLIB
import math
import random
import itertools
import sys
import thread
import time
from datetime import datetime, timedelta

# PONG CODES
from collision import *
from configs import *
from surface import *

def game_thread(surface, ball, paddles):

	VEL_MIN = 100
	VEL_MAX = 500
	VEL_INC = 250

	ball.xVel = random.randint(VEL_MIN, VEL_MAX)
	ball.yVel = random.randint(VEL_MIN, VEL_MAX)

	paddleLastCollided = -1

	while True:
		y = ball.y
		yVel = ball.yVel
		x = ball.x
		xVel = ball.xVel

		y += yVel
		x += xVel

		if surface.isAbove(y, ball):
			y = surface.topMost(ball)
			yVel *= -1

		elif surface.isBelow(y, ball):
			y = surface.bottomMost(ball)
			yVel *= -1

		if surface.isLeft(x, ball):
			x, y = (0, 0)
			xVel = random.randint(VEL_MIN, VEL_MAX) * -1
			yVel = random.randint(VEL_MIN, VEL_MAX) * -1

		elif surface.isRight(x, ball):
			x, y = (0, 0)
			xVel = random.randint(VEL_MIN, VEL_MAX)
			yVel = random.randint(VEL_MIN, VEL_MAX)

		for i in range(len(paddles)):
			paddle = paddles[i]
			if is_collision(ball, paddle) and paddleLastCollided != i:
				paddleLastCollided = i
				xVel *= -1
				xVel += VEL_INC
				yVel += VEL_INC
				print "Collide"

		#print x, y, "grid",  surface.inCell(x, y)
		#coord = surface.getGridCenter(surface.inCell(x, y))
		#cell = surface.inCell(x, y)
		#grid[0].x = coord[0]
		#grid[0].y = coord[1]

		#print "cell", cell

		ball.y = y
		ball.yVel = yVel
		ball.x = x
		ball.xVel = xVel

		time.sleep(0.02) # Keep this thread from hogging CPU

