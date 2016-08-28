#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    int j;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout<<setw(n-i);
        j = i+1;
        while(j--)
            cout<<"#";
        cout<<endl;
    }
    return 0;
}
