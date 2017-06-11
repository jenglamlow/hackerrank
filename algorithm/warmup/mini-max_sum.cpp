#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> arr(5);
    for(int arr_i = 0; arr_i < 5; arr_i++){
       cin >> arr[arr_i];
    }

    long long int sum(0);
    auto min = min_element(begin(arr), end(arr));
    auto max = max_element(begin(arr), end(arr));

    for (const auto& n : arr) {
        sum += n;
    }

    cout << sum - *max << " " << sum - *min;
    return 0;
}

