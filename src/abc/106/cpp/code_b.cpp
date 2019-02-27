#include <iostream>
int main(int argc, char const *argv[]) {
    int N;
    std::cin >> N;
    int c;
    int ans = 0;
    for (int i = 1; i < N + 1; i++) {
        if (i % 2 != 0) {
            c = 0;
            for (int j = 1; j < i + 1; j++) {
                if (i % j == 0) {
                    c++;
                }
            }
            if (c == 8) {
                ans++;
            }
        }
    }
    std::cout << ans << '\n';
    return 0;
}
