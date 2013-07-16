# STDLIB
import math
import sys

# TODO: Code won't work yet.
# TODO: Code cleanup

def collide(circle, rectangle):
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

	closestX = clamp(circle.x, paddle.x - padde.width/2, paddle.x + paddle.width/2)
	closestY = clamp(circle.y, paddle.y - padde.height/2, paddle.y + paddle.height/2)

	distX = circle.x - closestX
	distY = circle.y - closestY

	distSq = distX**2 + distY**2
	radSq = circle.radius**2

	# If dist less than radius, intersect!
	return distSq < radSq

