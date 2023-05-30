import numpy as np

import gradient
import lab1_methods.fibonacci as fib_lab1
import lab1_methods.golden_ratio as gr_lab1
import matplotlib.pyplot as plt
import StepFunctions as stepFunc

# const
start = -20
end = 20
const_epsilon = 0.00001
x = np.array([end, end])
const_array = np.array([100, 100])
args = np.meshgrid(np.arange(start, end, 0.1), np.arange(start, end, 0.1))


def gradient_test1(arg):
    return np.array(
        [4 * arg[0] + 4 * arg[1],
         4 * arg[0] + 12 * arg[1]]
    )


def function_test1(arg):
    return 2 * arg[0] ** 2 + \
           4 * arg[0] * arg[1] + \
           6 * arg[1] ** 2


def create_plot(name, function):
    print(name)
    coordinate, iteration, array = gradient.gradient(x, function_test1, gradient_test1, const_epsilon, function)
    print("Coordinate minimum: ", coordinate)
    print("Count iteration: ", iteration)
    arr = []
    for i in array:
        arr.append(i)

    print("Average speed convergence: ", np.mean(arr))
    t, a = plt.subplots(nrows=1, ncols=1)
    a.contour(*args, function_test1(args), 10)
    a.plot(*np.array(array).T)


def start():
    create_plot("Constant step", stepFunc.const_step)
    create_plot("Step Split", stepFunc.step_split)
    create_plot("Golden Ratio", stepFunc.step_golden_ratio)
    create_plot("Fibonacci", stepFunc.step_fibonacci)

    result, iteration = gradient.conjugate_gradient(gradient_test1, function_test1, const_epsilon, x, const_array, gr_lab1.golden_ratio)
    print("Conjugate gradient method")
    print("Minimum: ", result[len(result) - 1])
    print("Count iteration: ", iteration)

    coordinate, iteration, result = gradient.gradient(x, function_test1, gradient_test1, const_epsilon, stepFunc.step_golden_ratio)
    print("Gradient Descent Method")
    print("Minimum ", coordinate)
    print("Count iteration: ", iteration)

    plt.show()


if __name__ == "__main__":
    start()
