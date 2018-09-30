#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    std::string s[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> s[i];
    }
    for (size_t i = 0; i < N; i++) {
        for (size_t j = 0; j < N; j++) {
            std::cout << s[N - 1 - j][i];
        }
        std::cout << '\n';
    }

    return 0;
}
