#include <iostream>
#include <cmath>

#include "dichotomy.h"
#include "goldenRatio.h"
#include "fibonacci.h"
#include "parabola.h"
#include "brent.h"

double func(double x) {
    return (sin(x) * pow(x, 3));
}

void test(double a, double b, double eps) {
    std::cout << "New test: a = " << a << ", b = "  << b << ", eps = " << eps << std::endl;

    dichotomy(func, a, b, eps);
    goldenRatio(func, a, b, eps);
    fibonacci(func, a, b, eps);
    brent(func, a, b, eps);
    parabola(func, a, b, eps);

    std::cout << std::endl;
}

int main() {
    // test(-6.0, 0, 0.00001);
    // test(4.0, 6.0, 0.00001);
    // test(1.0, 10.0, 0.00001);
    // test(1.0, 9.0, 0.00001);
    // test(-37.0, 0.0, 0.00001);
    test(-37.0, -30.0, 0.00001);
    return 0;
}
