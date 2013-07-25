# STDLIB
import math
import random
import itertools
from datetime import datetime, timedelta
import time # for sleep

# PYGAME
import pygame

# PONG CODES
from configs import *
from collision import *
from controller import *

def controller_thread(surface, paddles):
	pygame.joystick.init()
	pygame.display.init()

	PADDLE_VEL = (math.sqrt(surface.getArea()) / 10) * PADDLE_VEL_MULT

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

			y += vert * PADDLE_VEL * -1

			if surface.isAbove(y, paddle):
				y = surface.topMost(paddle)
			elif surface.isBelow(y, paddle):
				y = surface.bottomMost(paddle)

			paddle.y = y


		time.sleep(0.02) # Keep this thread from hogging CPU

