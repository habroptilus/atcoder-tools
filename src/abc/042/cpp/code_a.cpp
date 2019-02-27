#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    int a, b, c;
    std::cin >> a >> b >> c;
    if (a == 5 && b == 5 && c == 7) {
        std::cout << "YES" << '\n';
    } else if (a == 5 && b == 7 && c == 5) {
        std::cout << "YES" << '\n';
    } else if (a == 7 && b == 5 && c == 5) {
        std::cout << "YES" << '\n';
    } else {
        std::cout << "NO" << '\n';
    }

    return 0;
}
