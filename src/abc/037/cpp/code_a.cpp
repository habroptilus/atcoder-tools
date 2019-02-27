#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    ll A, B, C;
    std::cin >> A >> B >> C;
    std::cout << C / std::min(A, B) << '\n';
    return 0;
}
