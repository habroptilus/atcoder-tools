#include <bits/stdc++.h>
typedef long long ll;

bool check(ll *d, ll x, ll K) {
    std::string s = std::to_string(x);
    for (size_t i = 0; i < K; i++) {
        if ((int)s.find(std::to_string(d[i])) != -1) {
            return false;
        }
    }
    return true;
}

int main(int argc, char const *argv[]) {
    ll N, K;
    std::cin >> N >> K;
    ll D[K];
    for (size_t i = 0; i < K; i++) {
        std::cin >> D[i];
    }
    ll ans = N;
    while (true) {
        if (check(D, ans, K)) {
            std::cout << ans << '\n';
            break;
        }
        ans++;
    }
    return 0;
}
