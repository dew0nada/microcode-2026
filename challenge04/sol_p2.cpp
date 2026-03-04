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

    int K;
    fin >> K;

    int sol = 0;
    for (int i = 0; i < n; ++i) {
        int p = (a[i] - 1) * (K + 1) + 1;
        sol = max(sol, p);
    }

    cout << sol << endl;
    return 0;
}