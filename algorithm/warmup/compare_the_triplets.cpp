#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void compare(int x, int y, int (&score)[2])
{
    if (x > y)
        score[0]++;
    else if (x < y)
        score[1]++;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a0, a1, a2;
    int b0, b1, b2;
    int score[2] = {0, 0};

    cin >> a0 >> a1 >> a2 >> b0 >> b1 >> b2;

    compare(a0, b0, score);
    compare(a1, b1, score);
    compare(a2, b2, score);

    cout << score[0] << " " << score[1] << endl;

    return 0;
}
