#include <iostream>
#include <algorithm>

int main(int argc, char const *argv[]) {
    int A,B,C;
    std::cin >> A>>B>>C;
    int g = std::__gcd(A,B);
    if (C%g==0) {
        std::cout << "YES" << '\n';
    }else{
        std::cout << "NO" << '\n';
    }

    return 0;
}
