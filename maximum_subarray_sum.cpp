#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int q, n;
    long long m, v, best, partial_sum, candidate;
    set<long long> partials;
    set<long long>::iterator partial_it;

    cin >> q;
    while (q--) {
        cin >> n >> m;
        set<long long>().swap(partials);   
        partial_sum = best = 0;
        for (int i = 0; i < n; ++i) {
            cin >> v;
            partial_sum = (partial_sum + v) % m;
            partial_it = partials.upper_bound(partial_sum);
            if (partial_it == partials.end()) {
                candidate = partial_sum;
            } else {
                candidate = m + partial_sum - *partial_it;
            }
            if (best < candidate) best = candidate;
            partials.insert(partial_sum);            
        }
        cout << best << '\n';
    }
    
    return 0;
}
