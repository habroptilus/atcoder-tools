#include <algorithm>
#include <iostream>
int main(int argc, char const *argv[]) {
    int N;
    std::cin >> N;
    int partition[9] = {400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 100000};
    int counts[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (size_t i = 0; i < N; i++) {
        int rate;
        std::cin >> rate;
        for (size_t j = 0; j < 9; j++) {
            if (rate < partition[j]) {
                counts[j]++;
                break;
            }
        }
    }

    int min = 0;
    int max;
    for (size_t i = 0; i < 8; i++) {
        if (counts[i] != 0) {
            min++;
        }
    }

    if (min == 0) {
        min = 1;
        max = counts[8];
        std::cout << min << " " << max << '\n';
    } else {
        max = min + counts[8];
        std::cout << min << " " << max << '\n';
    }
    return 0;
}
