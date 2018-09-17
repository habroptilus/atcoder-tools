#include <bits/stdc++.h>
typedef long long ll;

ll solve(ll *x, ll A, ll n) { // bit全探索する.200点取れるけど300点は取れない
    ll ans = 0;
    for (ll bit = 1; bit < (1 << n); ++bit) {
        std::vector<int> bit_set;
        for (int i = 0; i < n; ++i) {
            if (bit & (1 << i)) { // i が bit に入るかどうか
                bit_set.push_back(i);
            }
        }
        ll sum = 0;
        for (int i = 0; i < bit_set.size(); ++i) {
            sum += x[bit_set[i]];
        }
        if (sum == A * bit_set.size()) {
            ans++;
        }
    }
    return ans;
}

int main(int argc, char const *argv[]) {
    ll N, A;
    std::cin >> N >> A;
    ll x[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> x[i];
    }
    std::cout << solve(x, A, N) << '\n';
    return 0;
}
