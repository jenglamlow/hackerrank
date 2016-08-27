#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    long long int N, i, sum=0, num;
    cin >> N;
    for (i = 0; i < N; i++)
    {
        cin >> num;
        sum += num;
    }

    cout << sum << endl;

    return 0;
}