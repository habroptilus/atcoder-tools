#include <algorithm>
#include <iostream>

int main(int argc, char const *argv[]) {
    int N;
    std::cin >> N;
    int a[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    std::sort(a, a + N);
    std::cout << a[N - 1] - a[0] << '\n';
    return 0;
}
