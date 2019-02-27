#include <iostream>
int main(int argc, char const *argv[]) {
    long long s,c;std::cin >> s >> c;
    if (2*s>=c) {
        std::cout << c/2 << '\n';
    }else{
        std::cout << s+(c-2*s)/4 << '\n';
    }
    return 0;
}
