#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    std::string S;
    std::cin >> S;
    for (size_t i = 0; i < S.size(); i++) {
        if (S[i] == '9') {
            std::cout << '1';
        } else if (S[i] == '1') {
            std::cout << '9';
        } else {
            std::cout << S[i];
        }
    }
    std::cout << '\n';
    return 0;
}
