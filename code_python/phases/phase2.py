"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import numpy as np
from scipy.integrate import odeint

from myLib import generate


def model(F, t, f, gamma):
    R, M = F
    # f, gamma = params
    dR = M - f * R
    dM = f * gamma * R - M
    return [dR, dM]


def populate(R_0: float, M_0: float, f: float, gammas: list[float], t: int) \
        -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    Rs: list[np.ndarray] = []
    Ms: list[np.ndarray] = []
    ts: np.ndarray = np.linspace(0, t, num=t + 1)
    for gamma in gammas:
        for _ in range(t):
            sol = odeint(model, [R_0, M_0], ts, args=(f, gamma))
            Rs.append(np.array(sol[:, 0]))
            Ms.append(np.array(sol[:, 1]))
            pass
        pass
    return ts, np.array(Rs), np.array(Ms)


def main(R_0: float, M_0: float, f: float, gammas: list[float], t: int) -> \
        None:
    ts, Rs, Ms = populate(R_0, M_0, f, gammas, t)
    generate.plot(ts, Rs, R_0, gammas, "Linear Differential Model")
    return None
