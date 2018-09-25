#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    std::string S;
    std::cin >> S;
    std::string piano = "WBWBWWBWBWBW";
    std::string P;
    for (size_t i = 0; i < 3; i++) {
        P += piano;
    }
    std::vector<std::string> ans = {"Do",   "hoge", "Re",   "hoge",
                                    "Mi",   "Fa",   "hoge", "So",
                                    "hoge", "La",   "hoge", "Si"};
    bool flag;
    for (size_t i = 0; i < piano.size(); i++) {
        flag = true;
        for (size_t j = 0; j < S.size(); j++) {
            if (P[i + j] != S[j]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            std::cout << ans[i] << '\n';
            break;
        }
    }
    return 0;
}
