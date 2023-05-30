#include "dichotomy.h"

void dichotomy(double (*f)(double), double a, double b, double eps) {

    int iterationСount = 0;
    double delta = eps / 2;

    while (b - a > eps) {
        iterationСount += 1;
        double center = (a + b) / 2;

        double x1 = center - delta;
        double x2 = center + delta;

        if (f(x1) < f(x2)) { 
            b = x1;
        }
        else if (f(x1) > f(x2)) {
            a = x2;
        }
        else {
            a = x1;
            b = x2;
        }
    }

    double middle = (a + b) / 2;
    std::cout << "Dichotomy: " <<  f(middle) << "\t iterationCount: " << iterationСount << std::endl;
}

