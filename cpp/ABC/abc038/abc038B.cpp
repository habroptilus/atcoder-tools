#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll H_1, W_1, H_2, W_2;
    std::cin >> H_1 >> W_1 >> H_2 >> W_2;
    if (H_1 == H_2 || H_1 == W_2 || W_1 == H_2 || W_1 == W_2) {
        std::cout << "YES" << '\n';
    } else {
        std::cout << "NO" << '\n';
    }
    return 0;
}
