#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll a[N];
    ll mean = 0;
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
        mean += a[i];
    }
    mean = std::round((double)mean / N);
    ll ans = 0;
    for (size_t i = 0; i < N; i++) {
        ans += (a[i] - mean) * (a[i] - mean);
    }
    std::cout << ans << '\n';

    return 0;
}
