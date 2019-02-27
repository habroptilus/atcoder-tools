#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N, K;
    std::cin >> N >> K;
    std::cout << K * ll(std::pow(K - 1, N - 1)) << '\n';
    return 0;
}
