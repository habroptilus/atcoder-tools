#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll T = 3;
    for (size_t x = 1; x < 100; x++) {
        if (std::ceil((double)x / T) != (x + T - 1) / T) {
            std::cout << std::ceil((double)x / T) << '\n';
            std::cout << (x + T - 1) / T << '\n';
        }
    }
    ll y = 10000000000000;
    std::cout << typeid(std::ceil((double)y / T)).name() << '\n';
    std::cout << std::ceil((double)y / T) << '\n';
    std::cout << (y + T - 1) / T << '\n';

    double hoge = 1.0;
    ll fuga = 2;
    std::cout << typeid(hoge * fuga).name() << '\n';
    return 0;
}
