# STDLIB
import math
import random
import itertools
from datetime import datetime, timedelta
import time # for sleep

# PONG CODES
from collision import *
from configs import *
from surface import *

def game_thread(surface, ball, paddles):

	VEL_MIN = 100
	VEL_MAX = 500
	VEL_INC = 50

	ball.xVel = random.randint(VEL_MIN, VEL_MAX)
	ball.yVel = random.randint(VEL_MIN, VEL_MAX)

	paddleLastCollided = -1

	isRestarting = True
	lastOut = datetime.now()
	outWait = timedelta(milliseconds=500)

	while True:
		x = ball.x
		y = ball.y
		xVel = ball.xVel
		yVel = ball.yVel
		xVelMag = abs(ball.xVel)
		yVelMag = abs(ball.yVel)
		xVelSign = 1 if ball.xVel >= 0 else -1
		yVelSign = 1 if ball.yVel >= 0 else -1

		if isRestarting:
			if datetime.now() < lastOut + outWait:
				time.sleep(0.02) # Keep this thread from hogging CPU
				continue
			else:
				xVel = random.randint(VEL_MIN, VEL_MAX)
				yVel = random.randint(VEL_MIN, VEL_MAX)
				isRestarting = False

		x += xVel
		y += yVel

		hitPaddle = False

		for i in range(len(paddles)):
			paddle = paddles[i]
			if is_collision(ball, paddle) and paddleLastCollided != i:
				paddleLastCollided = i
				xVelMag += VEL_INC
				yVelMag += VEL_INC
				xVel = xVelMag * xVelSign * -1
				x = paddle.x

				hitPaddle = True
				break

		if not hitPaddle:
			if surface.isAbove(y, ball):
				y = surface.topMost(ball)
				yVel *= -1

			elif surface.isBelow(y, ball):
				y = surface.bottomMost(ball)
				yVel *= -1

			if surface.isLeft(x, ball):
				x, y = (0, 0)
				lastOut = datetime.now()
				isRestarting = True

			elif surface.isRight(x, ball):
				x, y = (0, 0)
				lastOut = datetime.now()
				isRestarting = True

		ball.x = x
		ball.y = y
		ball.xVel = xVel
		ball.yVel = yVel

		time.sleep(0.02) # Keep this thread from hogging CPU

