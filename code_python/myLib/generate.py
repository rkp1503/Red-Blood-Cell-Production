"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import os

import matplotlib.pyplot as plt
import numpy as np


def save_figure(filename: str):
    path_to_project_dir: str = os.path.dirname(os.getcwd())
    path_to_report_dir: str = os.path.join(path_to_project_dir, "report")
    path_to_figs_dir: str = os.path.join(path_to_report_dir, "figures")
    if os.path.exists(path_to_figs_dir):
        path_to_fig: str = os.path.join(path_to_figs_dir, filename)
        plt.savefig(f"{path_to_fig}.png", bbox_inches="tight")
        plt.savefig(f"{path_to_fig}.eps", bbox_inches="tight")
        pass
    pass


def plot(ts: np.ndarray, ys: np.ndarray, R_0: float, gammas: list[float],
         filename: str) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    graphs = []
    for y, gamma in zip(ys, gammas):
        temp_graph = plt.plot(ts, y / R_0, label=f"\u03B3={str(gamma)}",
                              linestyle='-', marker='o', markersize=1)
        graphs += temp_graph
        pass
    labels = [graph.get_label() for graph in graphs]
    ax.legend(graphs, labels, bbox_to_anchor=(1.01, 1.015), loc='upper left')
    plt.xlabel("Time in Days")
    plt.ylabel("Percentage of Red Blood Cell Population")
    plt.title(f"Red Blood Cell Population over {len(ts) - 1} Days")
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    save_figure(filename)
    plt.show()
    return None
