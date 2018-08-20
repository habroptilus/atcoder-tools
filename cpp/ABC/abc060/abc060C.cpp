#include <iostream>
#include <algorithm>


int main(int argc, char const *argv[]) {
    int N,T; std::cin >> N >> T;
    int t[N];

    for (size_t i = 0; i < N; i++) {
        std::cin >> t[i];
    }
    int s=0;

    for (size_t i = 0; i < N-1; i++) {
        s+= std::min(T,t[i+1]-t[i]);
    }

    s+=T;
    std::cout << s << '\n';



    return 0;
}
