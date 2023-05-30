import numpy as np


def gradient(x, function, gradient_function, eps, step_function):
    iteration = 0
    p = [i + 1 for i in x]
    a = 0
    array = []

    while abs(function(x) - function(p)) >= eps:
        iteration += 1
        p = x
        gradient1 = gradient_function(x)
        a = step_function(iteration, function, gradient1, p, a)
        x = [
                x[i] - a * gradient1[i]
                for i in range(len(x))
             ]

        array.append(np.array(x))
    return x, iteration, array


def conjugate_gradient(gradient1, function, eps, x, const_array, method1):
    r = np.zeros(len(x))
    a = 0
    iteration = 0
    array = []

    while abs(function(x) - function(const_array)) > eps:
        iteration += 1
        r = (-gradient1(x) + a * r) / np.linalg.norm(-gradient1(x) + a * r)

        def f(v):
            return function(x + v * r)

        result = method1(f, 0, method(f), eps)
        alpha = (result[0] + result[1]) / 2
        const_array = x
        array.append(x)
        x = x + alpha * r
        a = np.dot(gradient1(x), gradient1(x) - gradient1(x - const_array)) / np.linalg.norm(const_array) ** 2

    return [array, iteration]


def method(function):
    y = 0.01
    a = 0
    while not (
            (function(a - y) > function(a)) &
            (function(a + y) > function(a))
    ):
        if function(a + y) > function(a):
            a = a - y / 2
        else:
            a = a + y / 2
    return a
