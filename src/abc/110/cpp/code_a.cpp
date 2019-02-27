#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll a, b, c;
    std::cin >> a >> b >> c;
    std::cout << 9 * std::max({a, b, c}) + a + b + c << '\n';
    return 0;
}
