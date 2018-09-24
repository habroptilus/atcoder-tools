#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    ll ans = 10000000000;
    std::cin >> N;
    for (ll i = 1; i < N + 1; i++) {
        ans = std::min(std::abs(i - N / i) + N % i, ans);
    }
    std::cout << ans << '\n';
    return 0;
}
