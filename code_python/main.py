"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

# ----------------------------------------------------------------------------
# 3rd party libraries
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

from myLib import generate
from phases import phase1
from phases import phase2
from phases import phase3

# ----------------------------------------------------------------------------
# Initializing parameters
# ----------------------------------------------------------------------------
# Number of Red Blood Cells in circulation on day 0
R_0: float = 100

# Number of Red Blood Cells produced by marrow on day 0
M_0: float = 100

# Fraction of Red Blood Cells removed by spleen
f: float = 0.5

# Production constant (number produced per number lost)
# gamma: float = 1
gammas: list[float] = [1, 0.5, 2]

# Population over t days
t: int = 100

phase1.main(R_0, M_0, f, gammas, t)
phase2.main(R_0, M_0, f, gammas, t)
phase3.main(R_0, M_0, gammas, t)
