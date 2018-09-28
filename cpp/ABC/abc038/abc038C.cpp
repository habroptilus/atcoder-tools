#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll a[N];
    ll s = 1;
    ll ans = 0;
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    for (size_t i = 0; i < N - 1; i++) {
        if (a[i] < a[i + 1]) {
            s++;
        } else {
            ans += s * (s + 1) / 2;
            s = 1;
        }
    }
    ans += s * (s + 1) / 2;
    std::cout << ans << '\n';
    return 0;
}
