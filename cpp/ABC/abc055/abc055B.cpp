#include <iostream>
#include <cmath>

int main(int argc, char const *argv[]) {
    int N; std::cin >> N;
    int ans=1;
    int mod = 1000000007;
    for (size_t i = 0; i < N; i++) {
        ans=ans*(i+1)%mod;
    }
    std::cout << ans << '\n';
    return 0;
}
