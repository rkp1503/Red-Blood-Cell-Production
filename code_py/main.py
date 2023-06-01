"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import matplotlib.pyplot as plt
import numpy as np


def graphPlot(p, p0, gammas, tMax, title):
    # Set x range
    x = np.arange(0, tMax + 1, 1)

    # # Graph of y = p0
    # y = p0 * np.power(x, 0)

    # Plot p and y in x range
    fig = plt.figure()
    ax = fig.add_subplot(111)

    lns = []

    for i in range(0, len(gammas)):
        temp_lns = plt.plot(x, p[i], label='\u03B3 = ' + str(gammas[i]),
                            linestyle='-', marker='o', markersize=1)
        lns += temp_lns

    # lns += plt.plot(x, y, label='equilibrium', linestyle='--', marker='o',
    #                 markersize=1)

    # Set the range of the graph
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.ylim(ymax=p[0][0] * 10)

    # Set labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Number of Red Blood Cells')
    plt.title('Red Blood Cell Population')

    # Set gridlines
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Display Legend
    labs = [ls.get_label() for ls in lns]
    ax.legend(lns, labs, loc='best')

    # Display graph
    # fig.savefig(str(title) + '.png')
    plt.show()
    return


#################################################################################
# Model 1 Code
#################################################################################


def model1(R, f, gamma):
    return (1 - f) * R + gamma * f * R


def population1(p0, r, gammas, tMax, title):
    # initialize p and set p[0]
    p = []
    for i in range(0, len(gammas)):
        ps = np.zeros((tMax + 1, 1), dtype=float)
        ps[0] = p0
        p.append(ps)

    # Loop through years, computing new values of p
    for i in range(0, len(gammas)):
        for j in range(0, tMax):
            p[i][j + 1] = model1(p[i][j], r, gammas[i])

    # Graph plot
    graphPlot(p, p0, gammas, tMax, title)
    return


def model1_main(p, r, gammas, tMax):
    title = "linear_difference"
    population1(p, r, gammas, tMax, title)
    pass


#################################################################################
# Model 2 Code
#################################################################################


def model2(R, gamma):
    f = 1 - (1 / (R + 1))
    return (1 - f) * R + gamma * f * R


def population2(p0, gammas, tMax, title):
    # initialize p and set p[0]
    p = []
    for i in range(0, len(gammas)):
        ps = np.zeros((tMax + 1, 1), dtype=float)
        ps[0] = p0
        p.append(ps)

    # Loop through years, computing new values of p
    for i in range(0, len(gammas)):
        for j in range(0, tMax):
            p[i][j + 1] = model2(p[i][j], gammas[i])

    # Graph plot
    graphPlot(p, p0, gammas, tMax, title)
    return


def model2_main(p, gammas, tMax):
    title = "nonlinear_difference"
    population2(p, gammas, tMax, title)
    pass


#################################################################################
# Main Code
#################################################################################


def main():
    """
    You can add more values to the list of gammas to generate more plots
    :return:
    """
    # Initialize some variables
    p = 100  # Initial population
    r = 0.5  # Growth rate per year
    gammas = [1, 0.5, 2]  # Number of Red Blood Cells produced per lost
    tMax = 10  # Population over t days

    model1_main(p, r, gammas, tMax)

    # r = 1 - (1 / (p + 1))  # Growth rate per year
    gamma = [1, 0.5, 2]  # Number of Red Blood Cells produced per lost
    model2_main(p, gamma, tMax)

    return


if __name__ == '__main__':
    main()