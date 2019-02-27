#include <iostream>

int main(int argc, char const *argv[]) {
    int a,b,c;
    std::cin >> a >> b >> c;
    if (a+c==2*b) {
        std::cout << "YES" << '\n';
    }else{
        std::cout << "NO" << '\n';
    }
    return 0;
}
