#include <iostream>
using namespace std;

/// Avem un numar de n trepte care se pot urca cate una sau cate 2 -> fibonacci

int fibonacci_taranesc(int n) {
    if (n == 0 || n == 1)
        return n;
    return fibonacci_taranesc(n - 1) + fibonacci_taranesc(n - 2);
} /// O(2^n)

int fibonacci_liniar(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    int tfv = 0, tv = 1, tn;
    for (int i = 2; i <= n; i++) {
        tn = tv + tfv;
        tfv = tv;
        tv = tn;
    }
    return tn;
} /// O(n)

struct matrix {
    int elems[2][2];
};

matrix multMat(matrix A, matrix B) {
    matrix C;
    C.elems[0][0] = A.elems[0][0] * B.elems[0][0] + A.elems[0][1] * B.elems[1][0];
    C.elems[0][1] = A.elems[0][0] * B.elems[0][1] + A.elems[0][1] * B.elems[1][1];
    C.elems[1][0] = A.elems[1][0] * B.elems[0][0] + A.elems[1][1] * B.elems[1][0];
    C.elems[1][1] = A.elems[1][0] * B.elems[0][1] + A.elems[1][1] * B.elems[1][1];
    return C;
}

matrix putereMat(matrix A, unsigned int n) {
    if (n == 0) {
        matrix identity = {{{1, 0}, {0, 1}}};
        return identity;
    }
    if (n % 2 == 1)
        return multMat(A, putereMat(A, n - 1));
    matrix C = putereMat(A, n / 2);
    return multMat(C, C);
}

int fibo_matrix(int n) {
    if (n == 0 || n == 1)
        return n;
    matrix A = {{{0, 1}, {1, 1}}};
    matrix C = putereMat(A, n - 1);
    return C.elems[1][1];
} /// O(log2(n))

int main() {
    int n;
    cin >> n;
    cout << "Fibonacci taranesc: " << fibonacci_taranesc(n) << endl;
    cout << "Fibonacci liniar: " << fibonacci_liniar(n) << endl;
    cout << "Fibonacci matrix: " << fibo_matrix(n) << endl;
    return 0;
}
