#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N, K;
    std::cin >> N >> K;
    ll a[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    ll ans = 0;

    for (ll i = 0; i < N; i++) {
        if (i >= K - 1 && N - i - 1 >= K - 1) {
            ans += a[i] * K;
        } else if (i < K - 1 && N - i - 1 < K - 1) {
            ans += a[i] * (N - K + 1);
        } else {
            ans += a[i] * (std::min(i, N - i - 1) + 1);
        }
    }
    std::cout << ans << '\n';
    return 0;
}
