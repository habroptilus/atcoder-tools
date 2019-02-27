#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll K, S;
    std::cin >> K >> S;
    ll z;
    ll count = 0;
    for (size_t x = 0; x < K + 1; x++) {
        for (size_t y = 0; y < K + 1; y++) {
            z = S - x - y;
            if (0 <= z && z <= K) {
                count++;
                // std::cout << x << y << z << '\n';
            }
        }
    }

    std::cout << count << '\n';
    return 0;
}
