/// Sa se calculeze radical de ordin n din x cu precizia epsilon

#include <iostream>
#include <cmath>
using namespace std;

double power(double x, unsigned int n) {
    if (n == 0) return 1;
    if (n % 2 == 0) {
        double p = power(x, n / 2);
        return p * p;
    }
    return x * power(x, n - 1);
}

double root(double x, unsigned int n, double e) {
    if (x == 0) return 0;
    double st = 0, dr = x;
    double mij = (st + dr) / 2;
    while (fabs(power(mij, n) - x) > e) {
        if (power(mij, n) < x) st = mij;
        else dr = mij;
        mij = (st + dr) / 2;
    }
    return mij;
}

int main() {
    double x, e;
    unsigned int n;
    cin >> x >> n >> e;
    cout << root(x, n, e);
    return 0;
}
