#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll a, b, c;
    std::cin >> a >> b >> c;
    std::cout << (((a * b) % 1000000007) * c) % 1000000007 << '\n';

    return 0;
}
