#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N, Q;
    std::cin >> N >> Q;
    ll L[Q];
    ll R[Q];
    for (size_t i = 0; i < Q; i++) {
        std::cin >> L[i] >> R[i];
    }
    ll imos[N];
    for (size_t i = 0; i < N; i++) {
        imos[i] = 0;
    }
    for (size_t i = 0; i < Q; i++) {
        imos[L[i] - 1]++;
        if (R[i] < N) {
            imos[R[i]]--;
        }
    }
    ll sum = 0;
    for (size_t i = 0; i < N; i++) {
        sum += imos[i];
        imos[i] = sum;
    }
    for (size_t i = 0; i < N; i++) {
        if (imos[i] % 2 == 0) {
            std::cout << 0;
        } else {
            std::cout << 1;
        }
    }
    std::cout << '\n';
    return 0;
}
