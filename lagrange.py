import math
import random
import plotmanager
import iomanager


class InterpolatableFunction:
    def __init__(self, str_rep, action):
        self.str_rep = str_rep
        self.action = action


def interpolate():
    actions = [(lambda arg: math.sin(arg), "sin(x)"),
               (lambda arg: 2 * arg ** 3 - arg ** 2 + 9, "2x^3 - x^2 + 9"),
               (lambda arg: 7 * math.log(arg) if arg > 0 else None, "7*ln(x)")]
    functions = [InterpolatableFunction(i[1], i[0]) for i in actions]

    function = functions[get_function_number(functions)-1]
    boundaries = {iomanager.get_digit("Введите границу a", iomanager.InputType.FLOAT),
                  iomanager.get_digit("Введите границу b", iomanager.InputType.FLOAT)}
    a, b = min(boundaries), max(boundaries)
    dot_count = 10

    (x_values, y_values) = generate_dots(dot_count, a, b, function)
    x_values, y_values = filer_invalid_dots(dot_count, x_values, y_values)
    dot_count = len(x_values)

    '''for i in range(dot_count):
        iomanager.write_debug(str(x_values[i]) + "\t |\t" + str(x_values[i]) + "\n")'''

    plotmanager.get_dots_graph(x_values, y_values, function.str_rep)
    new_x_values = [random.random()*(b-a)+a for i in range(100)]
    new_x_values.sort()
    plotmanager.get_polynomial_graph(new_x_values, get_polynomial(x_values, y_values), "L(x)")
    plotmanager.show_graphs()


def get_function_number(functions):
    iomanager.write_message("Выберите интегрируемую интерполируемую функцию:\n")
    number = 0
    functions = [f.str_rep for f in functions]
    for i in range(len(functions) - 1):
        iomanager.write_message("\t" + str(i + 1) + ") " + str(functions[i]) + "\n")
    iomanager.write_message("\t" + str(len(functions)) + ") " + str(functions[-1]))

    is_valid = False
    while not is_valid:
        number = iomanager.get_digit("Номер уравнения", iomanager.InputType.INTEGER)
        if number < 1 or number > len(functions):
            iomanager.write_error("Функция с таким номером не найдена!")
        else:
            is_valid = True
    return number


def generate_dots(n, a, b, function):
    arguments = [random.random()*(b-a)+a for i in range(n)]
    arguments.sort()
    values = [function.action(arg) for arg in arguments]
    return [arguments, values]


def filer_invalid_dots(counter, x_values, y_values):
    iomanager.write_message("\n")
    if y_values.count(None) >= 1:
        iomanager.write_error("Выбранный интервал вышел за область допустимых значений функции. ")
        iomanager.write_message("Часть сгенерированных точек будет потеряна!\n")
        while y_values.count(None) >= 1:
            x_values.pop(y_values.index(None))
            y_values.pop(y_values.index(None))
        iomanager.write_message("Сгенерированных точек осталось: " + str(counter - len(x_values))+"\n\n")
    return x_values, y_values


def get_polynomial(x_values, y_values):
    basic_polynomials = [get_basic_polynomial(x_values, i) for i in range(len(x_values))]

    def polynomial(x):
        sum = 0
        for i in range(len(x_values)):
            sum += y_values[i] * basic_polynomials[i](x)
        return sum
    return polynomial


def get_basic_polynomial(x_values, i):
    def basic_polynomial(x):
        numerator, denominator = 1, 1
        for j in range(len(x_values)):
            if j != i:
                numerator *= (x - x_values[j])
                denominator *= (x_values[i] - x_values[j])
        return numerator/denominator
    return basic_polynomial


