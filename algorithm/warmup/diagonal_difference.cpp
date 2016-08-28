#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, j;
    int primary_sum = 0;
    int secondary_sum = 0;

    cin >> N;
    j = N - 1;
    
    for (int i = 0; i < N; i++, j--)
    {
        vector<int> v;
        int input;
        for (int k = 0; k < N; k++)
        {
            cin >> input;
            v.push_back(input);
        }

        primary_sum += v[i];
        secondary_sum += v[j];

    }
    cout << abs(primary_sum - secondary_sum) << endl;
    return 0;
}

// Without array approach (from discussion)
// for(int j = 0; j < numInputs; j++){
//     for(int k = 0; k < numInputs; k++){
//         cin >> curInput;
//         if(j == k){
//             leftD += curInput;
//         }
//         if(j+k == (numInputs-1)){
//             rightD += curInput;
//         }
//     }
// }
// ans = abs(leftD-rightD);