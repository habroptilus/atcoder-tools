#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll a, b;
    char op;
    std::cin >> a >> op >> b;
    if (op == '+') {
        std::cout << a + b << '\n';
    } else {
        std::cout << a - b << '\n';
    }
    return 0;
}
