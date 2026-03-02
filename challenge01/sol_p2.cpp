// copy past ndiba t3 l bibs
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    ifstream file("example.txt"); 
    string l;
    getline(file, l);
    long long t = stoll(l);

    vector<pair<long long, int>> nums;
    int i = 0;

    while (getline(file, l)) {
        if (!l.empty()) {
            nums.push_back({stoll(l), i++});
        }
    }
    file.close();
    sort(nums.begin(), nums.end()); // min to max
    
    int n = nums.size();
    bool found = false;
    
    for (int i = 0; i < n - 2 && !found; i++) {
        long long a = nums[i].first;
        int idx_a = nums[i].second;
        
        int left = i + 1;
        int right = n - 1;

        // a+b+c > t case
        if (a + nums[left].first + nums[right].first > t) {
            continue;
        }
        
        while (left < right) {
            long long b = nums[left].first;
            long long c = nums[right].first;
            int idx_b = nums[left].second;
            int idx_c = nums[right].second;
            
            long long sum = a + b + c;
            
            if (sum == t) {
                if (idx_a != idx_b && idx_a != idx_c && idx_b != idx_c) {
                    long long dis = max({a, b, c}) - min({a, b, c});
                    if (dis >= 1000) {
                        cout << "sol: " << a * b * c << endl;
                        return (0);
                    }
                }
                left++;
                right--;
            }
            else if (sum < t) {
                left++;
            }
            else {
                right--;
            }
        }
    }

}
