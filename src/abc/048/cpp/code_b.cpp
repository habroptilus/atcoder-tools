#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll a, b, x;
    std::cin >> a >> b >> x;
    if (a % x == 0) {
        std::cout << (b - a - b % x) / x + 1 << '\n';
    } else {
        std::cout << (b - a - x + a % x - b % x) / x + 1 << '\n';
    }

    return 0;
}
