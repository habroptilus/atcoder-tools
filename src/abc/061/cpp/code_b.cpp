#include <iostream>

int main(int argc, char const *argv[]) {
    int N,M;
    std::cin >> N>>M;
    int C[N];
    for (size_t i = 0; i < N; i++ ) {
       C[i] = 0;
   }
    for (size_t i = 0; i < M; i++) {
        int a,b;
        std::cin >> a>>b;
        C[a-1]++;
        C[b-1]++;
    }
    for (size_t i = 0; i < N; i++) {
        std::cout << C[i] << '\n';
    }
    return 0;
}
