#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll a, b, c;
    std::cin >> a >> b >> c;
    ll max = std::max({a, b, c});
    if (a + b + c == max * 2) {
        std::cout << "Yes" << '\n';
    } else {
        std::cout << "No" << '\n';
    }

    return 0;
}
