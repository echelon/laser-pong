"""
Game Configuration.
	- Control the surface size, position.
	- The ball and paddle sizes, etc.
	- The velocities.
	- And so forth...
"""

DMAX = 30000

		# ===========================
		# BASIC SURFACE CONFIGURATION
		# ===========================

x_offset = -10000
y_offset = -10000

Y_MAX = DMAX / 5 + y_offset
Y_MIN = -DMAX / 5 + y_offset

X_MAX = DMAX / 5 + x_offset
X_MIN = -DMAX / 5 + x_offset

		# ==========================
		# VELOCITY MULTIPLIERS
		# ==========================

PADDLE_VEL_MULT = 1.0
BALL_VEL_INIT_MULT = 1.0
BALL_VEL_INC_MULT = 1.0

		# ==========================
		# ENTITY SIZE MULTIPLIERS
		# ==========================

BALL_RADIUS_MULT = 1.0
PADDLE_HEIGHT_MULT = 1.0
PADDLE_WIDTH_MULT = 1.0

		# ==========================
		# MORE SURFACE CONFIGURATION
		# ==========================

# Surface flip (x-flip is not extremely useful)
FLIP_X = False
FLIP_Y = False

# Draw walls? 
# Not necessary for interesting surfaces. (ie, billboards)
# Can be useful for debugging.
DRAW_WALLS = False
DRAW_SURFACE_BOX = True

