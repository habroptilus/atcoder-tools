#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    ll T, A;
    ll x = 1;
    ll y = 1;
    ll n;
    std::cin >> N;
    for (size_t i = 0; i < N; i++) {
        std::cin >> T >> A;
        // n = std::max(std::ceil((double)x / T), std::ceil((double)y / A));
        n = std::max((x + T - 1) / T, (y + A - 1) / A);
        x = n * T;
        y = n * A;
    }
    std::cout << x + y << '\n';
    return 0;
}
