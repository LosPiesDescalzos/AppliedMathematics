#include "parabola.h"

void parabola(double (*f)(double), double a, double c, double eps) {
    int iterationCount = 0;
    double b = (a + c) / 2;
    double fa = f(a);
    double fc = f(c);
    double fb = f(b);
    double u;
    
    while (c - a > eps) {
        iterationCount++;
        
        u = b - (pow(b - a, 2) * (fb - fc) - pow(b - c, 2) * (fb - fa)) 
            / (2 * ((b - a) * (fb - fc) - (b - c) * (fb - fa)));
        
        if (!(u >= a && u <= c)) {
            break;
        }

        if (abs(u - ((c - a) / 2)) < eps) {
            break;
        }

        double fu = f(u);
        if (fu > fb) {
            if (u > b) {
                c = u;
                fc = fu;
            }
            else {
                a = u;
                fa = fu;
            }
        }
        else {
            if (b > u) {
                c = b;
                fc = fb;
            }
            else {
                a = b;
                fa = fb;
            }
            
            b = u;
            fb = fu;
        }
    }
    

    std::cout << "Parabola: " << f(u) << "\t iterationCount: " << iterationCount << std::endl;
}
