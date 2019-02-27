#include <iostream>

int main(int argc, char const *argv[]) {
    long long N, K;
    std::cin >> N >> K;
    if (K % 2 != 0) {
        std::cout << (N / K) * (N / K) * (N / K) << '\n';
    } else {
        std::cout << (N / K) * (N / K) * (N / K) + ((N + K / 2) / K) *
                                                       ((N + K / 2) / K) *
                                                       ((N + K / 2) / K)
                  << '\n';
    }

    return 0;
}
