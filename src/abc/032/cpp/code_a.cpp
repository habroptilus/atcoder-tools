#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll a, b, n;
    std::cin >> a >> b >> n;
    while (true) {
        if (n % a == 0 && n % b == 0) {
            std::cout << n << '\n';
            break;
        }
        n++;
    }

    return 0;
}
