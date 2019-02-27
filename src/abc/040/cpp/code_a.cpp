#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll x, n;
    std::cin >> n >> x;
    std::cout << std::min(n - x, x - 1) << '\n';
    return 0;
}
