#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    std::set<ll> S;
    ll a;
    for (size_t i = 0; i < 3; i++) {
        std::cin >> a;
        S.insert(a);
    }
    std::cout << S.size() << '\n';
    return 0;
}
