#include "goldenRatio.h"

void goldenRatio(double (*f)(double), double a, double b, double eps) {
    int iterationCount = 0;
 
    double phi = 1 - (sqrt(5) - 1) * 0.5;
    double x1 = a + phi * (b - a);
    double x2 = a + (1 - phi) * (b - a);
    double fx1 = f(x1);
    double fx2 = f(x2);
    while (b - a >= eps) {
        iterationCount += 1;
        if (fx1 >= fx2) {
            a = x1;
            x1 = x2;
            fx1 = fx2;
            x2 = a + (1 - phi) * (b - a);
            fx2 = f(x2);
        } 
        else {
            b = x2;
            x2 = x1;
            fx2 = fx1;
            x1 = a + phi * (b - a);
            fx1 = f(x1);
        }
    }

    double middle = (a + b) / 2;
    std::cout << "Golden ratio: " << f(middle) << "\t iterationCount: " << iterationCount << std::endl;
} 
