#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N, Q;
    std::cin >> N >> Q;
    ll L[Q];
    ll R[Q];
    ll T[Q];
    ll a[N];
    for (size_t i = 0; i < N; i++) {
        a[i] = 0;
    }
    for (size_t i = 0; i < Q; i++) {
        std::cin >> L[i] >> R[i] >> T[i];
    }

    for (size_t i = 0; i < Q; i++) {
        for (size_t j = 0; j < R[i] - L[i] + 1; j++) {
            a[j + L[i] - 1] = T[i];
        }
    }
    for (size_t i = 0; i < N; i++) {
        std::cout << a[i] << '\n';
    }

    return 0;
}
