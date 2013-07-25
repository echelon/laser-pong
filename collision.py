# STDLIB
import math
import sys

def is_collision(circle, rectangle):
	"""
	Elegant circle/rectangle intersection algorithm
	http://stackoverflow.com/a/1879223
	"""
	def clamp(val, minVal, maxVal):
		if val < minVal:
			return minVal
		elif val > maxVal:
			return maxVal
		return val

	closestX = clamp(circle.x, rectangle.getAbsRight(), rectangle.getAbsLeft())
	closestY = clamp(circle.y, rectangle.getAbsBottom(), rectangle.getAbsTop())

	distX = circle.x - closestX
	distY = circle.y - closestY

	distSq = distX**2 + distY**2
	radSq = circle.radius**2

	# If dist less than radius, intersect!
	return distSq < radSq

