"""
Configs, params, and so forth.
"""

DMAX = 30000

		# ===========================
		# BASIC SURFACE CONFIGURATION
		# ===========================

Y_MAX = DMAX /5
Y_MIN = -DMAX /5 

X_MAX = DMAX / 2
X_MIN = -DMAX / 2

		# ==========================
		# 	VELOCITY MULTIPLIERS
		# ==========================

PADDLE_VEL_MULT = 1.0
BALL_VEL_INIT_MULT = 1.0
BALL_VEL_INC_MULT = 1.0

		# =========================
		# 	ENTITY SIZE MULTIPLIERS
		# =========================

BALL_RADIUS_MULT = 1.0

		# ==========================
		# MORE SURFACE CONFIGURATION
		# ==========================

# Surface flip
FLIP_X = False
FLIP_Y = False

# Draw walls? 
# Not necessary for interesting surfaces. (ie, billboards)
DRAW_WALLS = True

