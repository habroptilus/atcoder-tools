#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    std::string S;
    std::cin >> S;
    char prev = 'f';
    ll ans = 0;
    for (size_t i = 0; i < S.size(); i++) {
        if (S[i] != prev) {
            ans++;
        }
        prev = S[i];
    }
    std::cout << ans - 1 << '\n';
    return 0;
}
