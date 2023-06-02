"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import numpy as np

from myLib import generate


def model(Rs: list[float], Ms: list[float], f: float, gamma: float) -> \
        tuple[float, float]:
    R_i: float = (1 - f) * Rs[-1] + Ms[-1]
    M_i: float = gamma * f * Rs[-1]
    return R_i, M_i


def populate(R_0: float, M_0: float, f: float, gammas: list[float], t: int) \
        -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    Rs: list[np.ndarray] = []
    Ms: list[np.ndarray] = []
    ts: np.ndarray = np.linspace(0, t, num=t + 1)
    for gamma in gammas:
        rs_i: list[float] = [R_0]
        ms_i: list[float] = [M_0]
        for _ in range(t):
            sol: tuple[float, float] = model(rs_i, ms_i, f, gamma)
            rs_i.append(sol[0])
            ms_i.append(sol[1])
            pass
        Rs.append(np.array(rs_i))
        Ms.append(np.array(ms_i))
        pass
    return ts, np.array(Rs), np.array(Ms)


def main(R_0: float, M_0: float, f: float, gammas: list[float], t: int) -> \
        None:
    ts, Rs, Ms = populate(R_0, M_0, f, gammas, t)
    generate.plot(ts, Rs, R_0, gammas, "Linear Difference Model")
    return None
