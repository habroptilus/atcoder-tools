#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll a[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    ll C[N];
    C[0] = 0;
    C[1] = std::abs(a[1] - a[0]);
    for (size_t i = 2; i < N; i++) {
        C[i] = std::min(C[i - 1] + std::abs(a[i] - a[i - 1]),
                        C[i - 2] + std::abs(a[i] - a[i - 2]));
    }
    std::cout << C[N - 1] << '\n';
    return 0;
}
