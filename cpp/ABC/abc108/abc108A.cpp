#include <iostream>
int main(int argc, char const *argv[]) {
    int K;
    std::cin >> K;
    if (K % 2 == 0) {
        std::cout << K * K / 4 << '\n';
    } else {
        std::cout << K / 2 * (K / 2 + 1) << '\n';
    }
    return 0;
}
