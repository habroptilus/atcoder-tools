#include <iostream>

int main(int argc, char const *argv[]) {
    char a,b;
    std::cin >> a >> b;
    if (a==b) {
        std::cout << "H" << '\n';
    }else{
        std::cout << "D" << '\n';
    }
    return 0;
}
