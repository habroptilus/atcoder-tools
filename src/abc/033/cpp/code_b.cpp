#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll sum = 0;
    ll max_p = 0;
    std::string max_s;
    std::string s;
    ll p;
    for (size_t i = 0; i < N; i++) {
        std::cin >> s >> p;
        sum += p;
        if (p > max_p) {
            max_p = p;
            max_s = s;
        }
    }
    if (2 * max_p > sum) {
        std::cout << max_s << '\n';
    } else {
        std::cout << "atcoder" << '\n';
    }

    return 0;
}
