#include <iostream>
long long mod = 1000000007;
void update_list(int n, long long *c_list) {
    for (int i = 2; i < n + 1; i++) {
        int count = 0;
        while (n % i == 0) {
            count++;
            n /= i;
        }
        c_list[i] += count;
    }
}

int main(int argc, char const *argv[]) {
    int N;
    std::cin >> N;
    long long count_list[N + 1];
    for (size_t i = 0; i < N + 1; i++) {
        count_list[i] = 0;
    }
    for (int i = 2; i < N + 1; i++) {
        update_list(i, count_list);
    }

    long long ans = 1;
    for (size_t i = 0; i < N + 1; i++) {
        ans = ans * (count_list[i] + 1);
        ans = ans % mod;
    }
    std::cout << ans << '\n';
    return 0;
}
