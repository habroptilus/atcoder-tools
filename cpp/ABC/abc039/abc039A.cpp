#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll a, b, c;
    std::cin >> a >> b >> c;
    std::cout << 2 * (a * b + b * c + c * a) << '\n';
    return 0;
}
