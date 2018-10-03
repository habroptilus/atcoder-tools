#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll x, y;
    std::cin >> x >> y;
    if (x < y) {
        std::cout << "Better" << '\n';
    } else {
        std::cout << "Worse" << '\n';
    }
    return 0;
}
