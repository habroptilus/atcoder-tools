#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll A, B, C, D;
    std::cin >> A >> B >> C >> D;
    std::cout << std::max(A * B, C * D) << '\n';
    return 0;
}
