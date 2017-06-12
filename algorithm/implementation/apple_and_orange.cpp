#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int s;
    int t;
    cin >> s >> t;
    int a;
    int b;
    cin >> a >> b;
    int m;
    int n;
    cin >> m >> n;
    vector<int> apple(m);
    for(int apple_i = 0;apple_i < m;apple_i++){
       cin >> apple[apple_i];
    }
    vector<int> orange(n);
    for(int orange_i = 0;orange_i < n;orange_i++){
       cin >> orange[orange_i];
    }

    int nApple  = 0;
    int nOrange = 0;

    for (const auto& i: apple) {
        int d = a + i;
        if ((d >= s) && (d <= t)) {
            ++nApple;
        }
    }

    for (const auto& i: orange) {
        int d = b + i;
        if ((d >= s) && (d <= t)) {
            ++nOrange;
        }
    }

    cout << nApple << endl;
    cout << nOrange << endl;

    return 0;
}
