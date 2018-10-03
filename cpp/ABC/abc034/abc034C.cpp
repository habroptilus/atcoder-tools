#include <bits/stdc++.h>
typedef long long ll;

ll calc(ll a, ll b, ll p) {
    if (b == 0) {
        return 1;
    } else if (b % 2 == 0) {
        ll d = calc(a, b / 2, p);
        return (d * d) % p;
    } else {
        return (a * calc(a, b - 1, p)) % p;
    }
}

int main(int argc, char const *argv[]) {
    ll W, H;
    std::cin >> W >> H;
    ll a = 1;
    ll b = 1;
    ll c = 1;
    ll M = 1000000007;

    for (size_t i = 1; i <= W + H - 2; i++) {
        a = (a * i) % M;
    }
    for (ll i = 1; i <= W - 1; i++) {
        b = (b * calc(i, M - 2, M)) % M;
    }

    for (ll i = 1; i <= H - 1; i++) {
        c = (c * calc(i, M - 2, M)) % M;
    }
    std::cout << (((a * b) % M) * c) % M << '\n';
    return 0;
}
