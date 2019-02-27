#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll a[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    std::map<ll, ll> m{};
    std::set<ll> st;
    for (size_t i = 0; i < N; i++) {
        st.insert(a[i]);
    }
    ll count = 0;
    for (auto x : st) {
        m[x] = count;
        count++;
    }
    for (size_t i = 0; i < N; i++) {
        std::cout << m[a[i]] << '\n';
    }
    return 0;
}
