import math

def func(x):
    math.sin(x) * x * x * x

def parabola(function, left_border, right_border, error):
    x1 = left_border
    x3 = right_border
    iteration_counter = 0
    # number_digits_after_comma = len(str(error).split('.')[1]) + 1  # количество знаков после запятой
    while abs(x3 - x1) > error:
        x2 = (x1 + x3) / 2
        f1 = function(x1)
        f2 = function(x2)
        f3 = function(x3)
        u = x2 - ((x2 - x1) * (x2 - x1) * (f2 - f3) - (x2 - x3) * (x2 - x3) * (f2 - f1)) / (2 * ((x2 - x1) * (f2 - f3) -
                                                                                                 (x2 - x3) * (f2 - f1)))
        if u < x2:
            x3 = x2
        else:
            x1 = x2
        iteration_counter += 1

    return x1, x3, iteration_counter


print(parabola(func, 4, 6, 0.00001))
