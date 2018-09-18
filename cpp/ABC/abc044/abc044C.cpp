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

ll solve_dp(ll *x, ll A, ll n) {
    ll sum = 0;

    for (size_t i = 0; i < n; i++) {
        sum += x[i];
    }
    ll DP[n + 1][n + 1][sum + 1];
    for (size_t j = 0; j < n + 1; j++) {
        for (size_t k = 0; k < n + 1; k++) {
            for (size_t s = 0; s < sum + 1; s++) {
                if (j >= 1 && s < x[j - 1]) {
                    DP[j][k][s] = DP[j - 1][k][s];
                } else if (j >= 1 && s >= x[j - 1] && k >= 1) {
                    DP[j][k][s] =
                        DP[j - 1][k][s] + DP[j - 1][k - 1][s - x[j - 1]];
                } else if (s == 0 && j == 0 && k == 0) {
                    DP[j][k][s] = 1;
                } else {
                    DP[j][k][s] = 0;
                }
            }
        }
    }
    ll ans = 0;
    /*
    for (size_t i = 1; i < n + 1; i++) {
        for (size_t j = 1; j < sum + 1; j++) {
            std::cout << DP[n][i][j] << " ";
        }
        std::cout << '\n';
    }*/
    for (size_t i = 1; i < std::min(sum / A + 1, n + 1); i++) {
        ans += DP[n][i][i * A];
        // std::cout << i << " " << i * A << " " << DP[n][i][i * A] << '\n';
    };

    return ans;
}

int main(int argc, char const *argv[]) {
    ll N, A;
    std::cin >> N >> A;
    ll x[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> x[i];
    }
    std::cout << solve_dp(x, A, N) << '\n';
    return 0;
}
