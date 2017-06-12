#include <bits/stdc++.h>

using namespace std;

vector < int > solve(vector < int > grades){
    vector < int > result;

    for (const auto& g: grades) {
        if (g < 38) {
            result.push_back(g);
        }
        else {
            int factor = g / 5;
            if (((factor + 1)*5) - g < 3){
                result.push_back((factor + 1)*5);
            }
            else {
                result.push_back(g);
            }
        }
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> grades(n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       cin >> grades[grades_i];
    }
    vector < int > result = solve(grades);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? "\n" : "");
    }
    cout << endl;
    

    return 0;
}
