#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("data.txt");
    string line;
    getline(fin, line);

    vector<int> a;
    stringstream ss(line);
    string temp;
    while (getline(ss, temp, ',')) {
        a.push_back(stoi(temp));
    }

    int n = a.size();

    int ms = *max_element(a.begin(), a.end());

    int ma = 0;
    for (int i = 0; i < n; ++i) {
        int sum = a[i] + a[(i+1)%n];
        ma = max(ma, sum);
    }

    int sum = accumulate(a.begin(), a.end(), 0);
    int mr = (sum + (n/2) - 1) / (n/2);
    
    int sol = max({ms, ma, mr});
    cout << sol << endl;

    return 0;
}