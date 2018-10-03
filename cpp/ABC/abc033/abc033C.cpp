#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    std::string S;
    std::cin >> S;
    ll ans = 0;
    ll terms = 1;
    bool flag = false;
    for (size_t i = 0; i < S.size(); i++) {
        if (S[i] == '+') {
            terms++;
            if (flag) {
                ans++;
                flag = false;
            }
        }
        if (S[i] == '0') {
            flag = true;
        }
    }
    if (flag) {
        ans++;
    }
    std::cout << terms - ans << '\n';
    return 0;
}
