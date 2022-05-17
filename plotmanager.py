import numpy as np
import matplotlib.pyplot as plt


def get_dots_graph(x_values, y_values, str_representation):
    figure = plt.figure()
    ax = figure.add_subplot(1, 2, 1)
    ax.set_title("Сгенерированный набор точек")
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.scatter(x_values, y_values, marker='o', edgecolors='black', label=str_representation)
    ax.legend(loc="upper left")
    ax.grid(True)
    # return ax


def get_polynomial_graph(x_values, function, str_representation):
    figure = plt.figure()
    ax = figure.add_subplot(1, 2, 2)
    ax.set_title("График ")
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.plot(x_values, [function(x) for x in x_values], label=str_representation)
    ax.legend(loc="upper left")
    ax.grid(True)
    # return ax


def show_graphs():
    plt.show()
