#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll n;
    std::cin >> n;
    ll v[n];
    for (size_t i = 0; i < n; i++) {
        std::cin >> v[i];
    }
    std::map<ll, ll> even{};
    std::map<ll, ll> odd{};

    for (size_t i = 0; i < n; i++) {
        if (i % 2 == 0) {
            even[v[i]] += 1;
        } else {
            odd[v[i]] += 1;
        }
    }

    ll max_even = -100000000000;
    ll second_even = -1000000000;
    ll max_odd = -100000000000;
    ll second_odd = -1000000000;
    ll even_max_key;
    ll odd_max_key;
    for (auto x : even) {
        if (max_even < x.second) {
            second_even = max_even;
            max_even = x.second;
            even_max_key = x.first;
        } else if (second_even < x.second) {
            second_even = x.second;
        }
    }

    for (auto x : odd) {
        if (max_odd < x.second) {
            second_odd = max_odd;
            max_odd = x.second;
            odd_max_key = x.first;
        } else if (second_odd < x.second) {
            second_odd = x.second;
        }
    }

    ll ans = 0;
    if (odd_max_key != even_max_key) {
        std::cout << n - max_even - max_odd << '\n';
    } else if (second_odd < 0 && second_even < 0) {
        std::cout << max_even << '\n';
    } else {
        std::cout << std::min(n - max_even - second_odd,
                              n - max_odd - second_even)
                  << '\n';
    }
    return 0;
}
