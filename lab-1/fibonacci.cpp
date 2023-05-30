#include "fibonacci.h"

double Bine(int n) {
    return (1 / sqrt(5)) * (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n)); 
}

void fibonacci(double (*f)(double), double a, double b, double eps) {
    int iterationCount = 0;
    int n = (b - a) * 10;

    double x1 = a + Bine(n - 2) / Bine(n) * (b - a);
    double x2 = b - Bine(n - 2) / Bine(n) * (b - a);
    double fx1 = f(x1);
    double fx2 = f(x2);
    while (n > 0) {
        iterationCount += 1;
        n--;

        if(fx1 < fx2) {
            b = x2;
            x2 = x1;
            fx2 = fx1;
            x1 = a + Bine(n - 2) / Bine(n) * (b - a);
            fx1 = f(x1);
        }
        else {
            a = x1;
            x1 = x2;
            fx1 = fx2;
            x2 = b - Bine(n - 2) / Bine(n) * (b - a);
            fx2 = f(x2);
        }
    }
    
    double middle = (a + b) / 2;
    std::cout << "Fibonacci: " << f(middle) << "\t iterationCount: " << iterationCount << std::endl;
}
