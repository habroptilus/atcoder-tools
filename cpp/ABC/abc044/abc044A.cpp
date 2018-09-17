#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll X, Y, K, N;
    std::cin >> N >> K >> X >> Y;
    if (N <= K) {
        std::cout << N * X << '\n';
    } else {
        std::cout << (N - K) * Y + K * X << '\n';
    }
    return 0;
}
