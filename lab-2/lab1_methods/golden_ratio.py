from math import sqrt


def golden_ratio(function, left_border, right_border, eps):
    a = left_border
    b = right_border
    iteration_counter = 0
    phi = (3 - sqrt(5)) / 2

    x1 = a + phi * (b - a)
    x2 = b - phi * (b - a)

    first_value = function(x1)
    second_value = function(x2)

    while abs(b - a) > eps:
        if first_value > second_value:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            first_value = second_value
            second_value = function(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            second_value = first_value
            first_value = function(x1)

        iteration_counter += 1

    return a, b, iteration_counter


