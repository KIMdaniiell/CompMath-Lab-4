import numpy as np
import matplotlib.pyplot as plt


def draw_dots_graph(x_values, y_values, str_representation):
    figure = plt.figure()
    ax = figure.add_subplot(1, 2, 1)
    ax.set_title("Сгенерированный набор точек")
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.scatter(x_values, y_values, marker='o', edgecolors='black', label=str_representation)
    ax.legend(loc="upper left")
    ax.grid(True)


def draw_polynomial_graph(x_values, function, str_representation):
    figure = plt.figure()
    ax = figure.add_subplot(1, 2, 2)
    ax.set_title("График интерполирующей функции")
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.plot(x_values, [function(x) for x in x_values], label=str_representation)
    ax.legend(loc="upper left")
    ax.grid(True)


def draw_result(generated_x, generated_y, test_x, original_function, polynomial_function, str_representation):
    figure, axes = plt.subplots()
    axes.scatter(generated_x, generated_y, marker='o', edgecolors='black', label=str_representation)
    # axes.plot(generated_x, [original_function(x) for x in generated_x], label=str_representation)
    axes.plot(test_x, [original_function(x) for x in test_x], label=str_representation)
    axes.plot(test_x, [polynomial_function(x) for x in test_x], color="red", label="L(x)")
    axes.set_xlabel("Ось X")
    axes.set_ylabel("Ось Y")
    axes.legend(loc="upper left")
    axes.grid(True)
    return


def show_graphs():
    plt.show()
