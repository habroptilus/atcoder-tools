#include <bits/stdc++.h>
typedef long long ll;
typedef std::pair<ll, ll> pair;

int main(int argc, char const *argv[]) {
    std::vector<pair> v;
    ll N;
    std::cin >> N;
    ll a;
    for (ll i = 0; i < N; i++) {
        std::cin >> a;
        v.push_back(pair(i + 1, a));
    }
    std::sort(v.begin(), v.end(),
              [](pair p1, pair p2) { return p1.second > p2.second; });
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v[i].first << '\n';
    }
    return 0;
}
