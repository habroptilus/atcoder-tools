#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll A[N];
    ll mod = 1000000007;
    for (size_t i = 0; i < N; i++) {
        std::cin >> A[i];
    }

    std::map<ll, ll> m{};

    for (size_t i = 0; i < N; i++) {
        m[A[i]] += 1;
    }
    ll ans = 1;

    for (auto x : m) {
        if ((x.first == 0 && x.second != 1) ||
            (x.first != 0 && x.second != 2)) {
            std::cout << 0 << '\n';
            return 0;
        } else if (x.first != 0) {
            ans = (ans * 2) % mod;
        }
    }

    std::cout << ans << '\n';
    return 0;
}
