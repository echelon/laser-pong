"""
Most of the game logic is here, aside from controller/paddle movement.
"""

# STDLIB
import math
import random
import itertools
from datetime import datetime, timedelta
import time # for sleep

# PONG CODES
from configs import *
from collision import *
from surface import *


def game_thread(surface, ball, paddles):
	"""
	This function is run as a thread and defines the game logic.
	"""

	# Keep this thread from hogging CPU
	THREAD_SLEEP_TIME = 0.02

	VEL_MIN = (math.sqrt(surface.getArea()) / 50) * BALL_VEL_INIT_MULT
	VEL_INC = (VEL_MIN / 10) * BALL_VEL_INC_MULT

	ball.xVel = VEL_MIN
	ball.yVel = VEL_MIN

	paddleLastCollided = -1

	isRestarting = True
	lastOut = datetime.now()
	outWait1 = timedelta(milliseconds=300)
	outWait2 = timedelta(milliseconds=1000)

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
			if datetime.now() < lastOut + outWait1:
				ball.x = 0
				ball.y = 0
				ball.skipDraw = True
				time.sleep(THREAD_SLEEP_TIME)
				continue
			if datetime.now() < lastOut + outWait2:
				ball.x = 0
				ball.y = 0
				ball.skipDraw = False
				time.sleep(THREAD_SLEEP_TIME)
				continue
			else:
				xVel = VEL_MIN * (1 if random.randint(0, 1) else -1)
				yVel = VEL_MIN * (1 if random.randint(0, 1) else -1)
				paddleLastCollided = -1
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

			if surface.isLeft(x, ball) or surface.isRight(x, ball):
				print 'OUT!', 'cur->new', ball.x, x
				lastOut = datetime.now()
				isRestarting = True

		ball.x = x
		ball.y = y
		ball.xVel = xVel
		ball.yVel = yVel

		time.sleep(THREAD_SLEEP_TIME)

