#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll W, H;
    std::cin >> W >> H;
    if (W * 9 == H * 16) {
        std::cout << "16:9" << '\n';
    } else {
        std::cout << "4:3" << '\n';
    }
    return 0;
}
