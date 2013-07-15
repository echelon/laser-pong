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
#from ball import *
from paddle import *
from square import *

paddle1 = Square()
#paddle2 = Paddle()

#ps.objects.append(paddle2)

def dac_thread():
	global paddle1

	ps = PointStream()
	ps.objects.append(paddle1)

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

