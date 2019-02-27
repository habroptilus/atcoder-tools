#include <iostream>
#include <string>

int main(int argc, char const *argv[]) {
    std::string S;
    long long K;
    std::cin >> S;
    std::cin >> K;
    bool flag = true;
    for (size_t i = 0; i < S.size(); i++) {
        if (S[i] != '1') {
            if (K < i + 1) {
                std::cout << 1 << '\n';
            } else {
                std::cout << S[i] << '\n';
            }
            flag = false;
            break;
        }
    }
    if (flag) {
        std::cout << 1 << '\n';
    }
    return 0;
}
