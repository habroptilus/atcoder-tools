#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N, M;
    std::cin >> N;
    ll T[N];

    for (size_t i = 0; i < N; i++) {
        std::cin >> T[i];
    }
    std::cin >> M;
    ll P[M];
    ll X[M];
    for (size_t i = 0; i < M; i++) {
        std::cin >> P[i] >> X[i];
    }
    ll sum = 0;
    for (size_t i = 0; i < N; i++) {
        sum += T[i];
    }
    for (size_t i = 0; i < M; i++) {
        std::cout << sum - T[P[i] - 1] + X[i] << '\n';
    }
    return 0;
}
