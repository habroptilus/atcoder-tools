#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N, L;
    std::cin >> N >> L;
    std::string a;
    std::vector<std::string> s;
    for (size_t i = 0; i < N; i++) {
        std::cin >> a;
        s.push_back(a);
    }

    std::sort(s.begin(), s.end());
    for (size_t i = 0; i < s.size(); i++) {
        std::cout << s[i];
    }
    std::cout << '\n';
    return 0;
}
