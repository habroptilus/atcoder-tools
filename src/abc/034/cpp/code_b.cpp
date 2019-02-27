#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll n;
    std::cin >> n;
    if (n % 2 == 0) {
        std::cout << n - 1 << '\n';
    } else {
        std::cout << n + 1 << '\n';
    }
    return 0;
}
