#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll sx, sy, tx, ty;
    std::cin >> sx >> sy >> tx >> ty;
    ll dx = tx - sx;
    ll dy = ty - sy;
    for (size_t i = 0; i < dx; i++) {
        std::cout << "R";
    }
    for (size_t i = 0; i < dy; i++) {
        std::cout << "U";
    }
    for (size_t i = 0; i < dx; i++) {
        std::cout << "L";
    }
    for (size_t i = 0; i < dy; i++) {
        std::cout << "D";
    }
    std::cout << "D";
    for (size_t i = 0; i < dx + 1; i++) {
        std::cout << "R";
    }
    for (size_t i = 0; i < dy + 1; i++) {
        std::cout << "U";
    }
    std::cout << "LU";
    for (size_t i = 0; i < dx + 1; i++) {
        std::cout << "L";
    }
    for (size_t i = 0; i < dy + 1; i++) {
        std::cout << "D";
    }
    std::cout << "R"
              << "\n";
    return 0;
}
