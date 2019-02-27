#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    std::string S;
    std::cin >> N >> S;
    ll max = 0;
    ll x = 0;
    for (size_t i = 0; i < S.length(); i++) {
        if (S[i] == 'I') {
            x++;
            max = std::max(max, x);
        } else {
            x--;
        }
    }
    std::cout << max << '\n';
    return 0;
}
