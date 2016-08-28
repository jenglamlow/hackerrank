#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, input;
    int pos = 0, neg = 0, zero = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> input;
        if (input < 0)
            neg++;
        else if (input > 0)
            pos++;
        else
            zero++;
    }

    cout.precision(6);
    cout << float(pos)/float(N) << endl;
    cout << float(neg)/float(N) << endl;
    cout << float(zero)/float(N) << endl;
    return 0;
}
