"""
Configs, params, and so forth.
"""

DMAX = 30000

		# ===========================
		# BASIC SURFACE CONFIGURATION
		# ===========================

Y_MAX = DMAX /10
Y_MIN = -DMAX /10
X_MAX = DMAX /10
X_MIN = -DMAX /10

		# ==========================
		# 	VELOCITY MULTIPLIERS
		# ==========================

PADDLE_VEL_MULT = 1.0
BALL_VEL_INIT_MULT = 1.0
BALL_VEL_INC_MULT = 1.0

		# ==========================
		# MORE SURFACE CONFIGURATION
		# ==========================

# Surface flip
FLIP_X = True
FLIP_Y = True

# Draw walls? 
# Not necessary for interesting surfaces. (ie, billboards)
DRAW_WALLS = False

