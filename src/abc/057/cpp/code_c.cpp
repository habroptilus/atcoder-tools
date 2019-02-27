#include <iostream>
#include <cmath>
#include <string>

int main(int argc, char const *argv[]) {
    long long N;std::cin >> N;
    int sqrt_N;
    sqrt_N= std::sqrt(N);
    while (true) {
        if (N%sqrt_N==0) {
            std::cout << std::to_string(N/sqrt_N).length() << '\n';
            break;
        }
        sqrt_N-=1;
    }
    return 0;
}
