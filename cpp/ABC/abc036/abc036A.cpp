#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll A, B;
    std::cin >> A >> B;
    if (B % A == 0) {
        std::cout << B / A << '\n';
    } else {
        std::cout << B / A + 1 << '\n';
    }

    return 0;
}
