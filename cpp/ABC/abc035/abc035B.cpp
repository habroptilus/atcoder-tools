#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    std::string S;
    std::cin >> S;
    int T;
    std::cin >> T;
    ll x = 0;
    ll y = 0;
    ll q = 0;
    for (size_t i = 0; i < S.size(); i++) {
        switch (S[i]) {
        case 'U':
            y++;
            break;
        case 'D':
            y--;
            break;
        case 'R':
            x++;
            break;
        case 'L':
            x--;
            break;
        default:
            q++;
        }
    }

    if (T == 1) {
        std::cout << x + y + q << '\n';
    } else {
        std::cout << std::abs(x + y - q) << '\n';
    }
    return 0;
}
