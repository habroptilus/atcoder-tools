#include <algorithm>
#include <iostream>

long get_min(int X, int Y) {
    long S_a, S_b, S_c;
    long y;
    long min = 1000000000;
    for (size_t x = 1; x < X; x++) {
        S_a = x * Y;
        y = Y / 2;
        S_b = (X - x) * y;
        S_c = (X - x) * (Y - y);
        min = std::min(std::max({S_a, S_b, S_c}) - std::min({S_a, S_b, S_c}),
                       min);
    }
    return min;
}

int main(int argc, char const *argv[]) {
    int H, W;
    std::cin >> H >> W;

    if (H % 3 == 0 || W % 3 == 0) {
        std::cout << 0 << '\n';
    } else {
        int ans1 = get_min(H, W);
        int ans2 = get_min(W, H);
        int ans3 = W;
        int ans4 = H;

        std::cout << std::min({ans1, ans2, ans3, ans4}) << '\n';
    }

    return 0;
}
