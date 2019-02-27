#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N, X;
    std::cin >> N >> X;
    ll x[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> x[i];
    }
    ll ans = std::abs(X - x[0]);
    for (size_t i = 1; i < N; i++) {
        ans = std::__gcd(std::abs(X - x[i]), ans);
    }
    std::cout << ans << '\n';
    return 0;
}
