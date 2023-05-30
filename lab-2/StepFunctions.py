import lab1_methods.fibonacci as fib_lab1
import lab1_methods.golden_ratio as gr_lab1
import sympy

const_epsilon = 0.001
left = 0
right = 1000000


def const_step(iteration, function, gradient, prev, a):
    # default value
    if a == 0:
        a = 0.001

    if iteration % 10 == 0:
        a *= 2

    while function(prev) <= \
            function([prev[i] - a * gradient[i]
                      for i in range(len(prev))]):
        a /= 2
    return a


def step_split(iteration, function, gradient, prev, a):
    e = 0.1

    # default value
    if a == 0:
        a = 1
    while function(prev) - \
            function([prev[i] -
                      a * gradient[i]
                      for i in range(len(prev))]) < \
            e * a * sum([i ** 2 for i in gradient]):
        a *= 0.95
    return a


def step_golden_ratio(iteration, function, gradient, prev, a):
    a = sympy.symbols('a')
    a1, a2, a3 = gr_lab1.golden_ratio(sympy.lambdify(a, function([prev[i] - a * gradient[i] for i in range(len(prev))])), left, right, const_epsilon)
    return (a1 + a2) / 2


def step_fibonacci(iteration, function, gradient, prev, a):
    a = sympy.symbols('a')
    a1, a2, a3 = fib_lab1.fibonacci(sympy.lambdify(a, function([prev[i] - a * gradient[i] for i in range(len(prev))])), left, right, const_epsilon)
    return (a1 + a2) / 2
