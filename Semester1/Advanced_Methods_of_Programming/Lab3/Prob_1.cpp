#include <iostream>
#include <algorithm>
using namespace std;

struct triplet {
    int t1, t2, t3;
};

/// O(n^3) varianta bruta
void triplete_de_suma_s(int s, int list[], int l, triplet triplete[], int &index) {
    index = 0;
    for (int i = 0; i < l - 2; i++)
        for (int j = i + 1; j < l - 1; j++)
            for (int k = j + 1; k < l; k++)
                if (list[i] + list[j] + list[k] == s) {
                    triplete[index].t1 = list[i];
                    triplete[index].t2 = list[j];
                    triplete[index].t3 = list[k];
                    index++;
                }
}

/// O(n^2 * log n) -> sortare, 2 foruri si cb pt al treilea elem
bool cautareBinara(int list[], int l, int val, int stanga) {
    int dreapta = l - 1, mijloc;
    while (stanga <= dreapta) {
        mijloc = (stanga + dreapta) / 2;
        if (list[mijloc] == val)
            return true;
        if (list[mijloc] > val)
            dreapta = mijloc - 1;
        else
            stanga = mijloc + 1;
    }
    return false;
}

void suma_triplete(int s, int list[], int l, triplet triplete[], int &index) {
    index = 0;
    sort(list, list + l);
    for (int i = 0; i < l - 2; i++)
        for (int j = i + 1; j < l - 1; j++) {
            if (cautareBinara(list, l, s - (list[i] + list[j]), j + 1)) {
                triplete[index].t1 = list[i];
                triplete[index].t2 = list[j];
                triplete[index].t3 = s - (list[i] + list[j]);
                index++;
            }
        }
}

/// O(n^2) -> sortare, un for si st si dr celelalte 2 nr
void suma_triplete_greedy(int s, int list[], int l, triplet triplete[], int &index) {
    index = 0;
    sort(list, list + l);
    for (int i = 0; i < l - 2; i++) {
        int stanga = i + 1, dreapta = l - 1;
        while (stanga < dreapta) {
            int sum = list[i] + list[stanga] + list[dreapta];
            if (sum == s) {
                triplete[index].t1 = list[i];
                triplete[index].t2 = list[stanga];
                triplete[index].t3 = list[dreapta];
                index++;
                stanga++;
                dreapta--;
            }
            else if (sum > s)
                dreapta--;
            else
                stanga++;
        }
    }
}

int main() {
    int list[9] = {1, 5, 4, 10, 0, 0, 9, 1, 3};
    triplet triplete[100];
    int index;

    // Testing brute force method
    cout << "Brute Force Method:" << endl;
    triplete_de_suma_s(14, list, 9, triplete, index);
    for (int j = 0; j < index; j++)
        cout << triplete[j].t1 << ' ' << triplete[j].t2 << ' ' << triplete[j].t3 << endl;

    // Testing binary search method
    cout << "Binary Search Method:" << endl;
    suma_triplete(14, list, 9, triplete, index);
    for (int j = 0; j < index; j++)
        cout << triplete[j].t1 << ' ' << triplete[j].t2 << ' ' << triplete[j].t3 << endl;

    // Testing two-pointer method
    cout << "Two-pointer Method:" << endl;
    suma_triplete_greedy(14, list, 9, triplete, index);
    for (int j = 0; j < index; j++)
        cout << triplete[j].t1 << ' ' << triplete[j].t2 << ' ' << triplete[j].t3 << endl;

    return 0;
}
