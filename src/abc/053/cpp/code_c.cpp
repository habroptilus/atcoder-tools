#include <iostream>
int main(int argc, char const *argv[]) {
    long long x;
    std::cin >> x;
    long long a = x / 11;
    int b = x % 11;
    if (b > 6) {
        std::cout << 2 * a + 2 << '\n';
    } else if (b == 0) {
        std::cout << 2 * a << '\n';
    } else {
        std::cout << 2 * a + 1 << '\n';
    }
    return 0;
}
