#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N, M, X, Y;
    std::cin >> N >> M >> X >> Y;
    std::vector<ll> x;
    std::vector<ll> y;
    ll t;
    for (size_t i = 0; i < N; i++) {
        std::cin >> t;
        x.push_back(t);
    }
    for (size_t i = 0; i < M; i++) {
        std::cin >> t;
        y.push_back(t);
    }
    x.push_back(X);
    y.push_back(Y);
    if (*std::max_element(x.begin(), x.end()) <
        *std::min_element(y.begin(), y.end())) {
        std::cout << "No War" << '\n';
    } else {
        std::cout << "War" << '\n';
    }
    return 0;
}
