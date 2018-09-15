#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll H, W, N;
    std::cin >> W >> H >> N;
    ll x_min = 0;
    ll x_max = W;
    ll y_min = 0;
    ll y_max = H;
    ll x, y, a;
    for (size_t i = 0; i < N; i++) {
        std::cin >> x >> y >> a;
        if (a == 1) {
            x_min = std::max(x_min, x);
        } else if (a == 2) {
            x_max = std::min(x_max, x);
        } else if (a == 3) {
            y_min = std::max(y_min, y);
        } else {
            y_max = std::min(y_max, y);
        }
    }
    if (x_max > x_min && y_max > y_min) {
        std::cout << (x_max - x_min) * (y_max - y_min) << '\n';
    } else {
        std::cout << 0 << '\n';
    }
    return 0;
}
