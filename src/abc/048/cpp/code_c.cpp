#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N, x;
    std::cin >> N >> x;
    ll a[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    ll count = 0;
    for (size_t i = 0; i < N - 1; i++) {
        if (a[i] + a[i + 1] > x) {
            count += a[i] + a[i + 1] - x;
            if (x >= a[i]) {
                a[i + 1] = x - a[i];
            } else {
                a[i + 1] = 0;
                a[i] = x;
            }
        }
    }
    std::cout << count << '\n';
    return 0;
}
