#include "brent.h"

void brent(double (*f)(double), double a, double b, double eps) {
    int iterationCount = 0;
    
    double phi = (3 - sqrt(5)) / 2;
    
    double x = a + phi * (b - a);   
    double w = a + phi * (b - a);   
    double v = a + phi * (b - a);   
    double u;
    
    double fx = f(x);
    double fw = f(w);
    double fv = f(v);

    double currentD = b - a;
    double previosD = b - a;


    while ((x - a > b - x ? x - a : b - x) > eps) {
        iterationCount++;
 
        double g = previosD / 2;
        previosD = currentD;
        
        if (x != w && w != v && x != v && fx != fw && fx != fv && fv != fw) {
            u = w - (pow(w - x, 2) * (fw - fv) - pow(w - v, 2) * (fw - fx)) 
             / (2 * ((w - x) * (fw - fv) - (w - v) * (fw - fx)));
        }

        if (!(u > a + eps  && u < b - eps) || abs(u - x) < g / 2) {
            if (x < (a + b) / 2) {
                u = x + phi * (b - x);
                previosD = b - x;
            } 
            else {
                u = x - phi * (x - a);
                previosD = x - a;
            }
        }
 
        currentD = abs(u - x);
        double fu = f(u);
        
        if (fu <= fx) {
            if (u >= x) {
                a = x;
            }
            else {
                b = x;
            }

            v = w;
            w = x;
            x = u;
            fv = fw;
            fw = fx;
            fx = fu;
        }
        else {
            if (u >= x) {
                b = u;
            }
            else {
                a = u;
            }

            if (fu <= fw || w == x) {
                v = w;
                w = u;
                fv = fw;
                fw = fu;
            } 
            else if (fu <= fv || v == x || v == w) {
                v = u;
                fv = fu;
            }
        }
    }
 
    double middle = (a + b) / 2;
    std::cout << "Brent: " << f(middle) << " \t iterationCount: " << iterationCount << std::endl;
}
