#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N, T;
    std::cin >> N >> T;
    ll c[N];
    ll t[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> c[i] >> t[i];
    }

    ll ans = 100000;
    for (size_t i = 0; i < N; i++) {
        if (t[i] <= T && c[i] < ans) {
            ans = c[i];
        }
    }
    if (ans == 100000) {
        std::cout << "TLE" << '\n';
    } else {
        std::cout << ans << '\n';
    }

    return 0;
}
