/// Se da un nr x > 1. Sa se aproximeze radical din x cu o precizie epsilon
#include<iostream>
#include<cmath>
using namespace std;

double sqrte(double x, double e) {
    double st = 1, dr = x;
    double mij = (st + dr) / 2;
    while (fabs(mij * mij - x) > e) {
        if (mij * mij < x) {
            st = mij;
        } else {
            dr = mij;
        }
        mij = (st + dr) / 2;
    }
    return mij;
}

int main() {
    double x, e;
    cin >> x >> e;
    cout << sqrte(x, e);
    return 0;
}
