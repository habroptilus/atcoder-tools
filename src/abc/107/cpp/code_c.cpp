#include <algorithm>
#include <iostream>
#include <vector>

void print(std::vector<long long> v) {
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v[i] << ' ';
    }
    std::cout << '\n';
}

int main(int argc, char const *argv[]) {
    int N, K;
    std::cin >> N >> K;
    std::vector<long long> R{0}, L;
    long long x;
    for (size_t i = 0; i < N; i++) {
        std::cin >> x;
        if (x > 0) {
            R.push_back(x);
        } else if (x < 0) {
            L.push_back(x);
        } else {
            K--;
        }
    }
    L.push_back(0);
    reverse(begin(L), end(L));

    long long ans = 100000000000000;
    for (size_t i = std::max(0, K + 1 - (int)L.size());
         i < std::min((int)R.size(), K + 1); i++) {
        ans = std::min({2 * R[i] - L[K - i], R[i] - 2 * L[K - i], ans});
    }
    std::cout << ans << '\n';
    return 0;
}
