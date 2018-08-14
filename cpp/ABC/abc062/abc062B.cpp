#include <iostream>
#include <string>

int main(int argc, char const *argv[]) {
    int H,W;
    std::cin >> H >> W;
    char a[H][W];
    for (size_t i = 0; i < H; i++) {
        for (size_t j = 0; j < W; j++) {
            std::cin >> a[i][j];
        }
    }
    std::string upper_frame(W+2,'#');
    std::cout << upper_frame << '\n';
    for (size_t i = 0; i < H; i++) {
        std::cout << "#";
        for (size_t j = 0; j < W; j++) {
            std::cout << a[i][j];
        }
        std::cout << "#" << '\n';
    }
    std::cout << upper_frame << '\n';

    return 0;
}
