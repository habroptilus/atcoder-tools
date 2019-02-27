#include <iostream>
int main(int argc, char const *argv[]) {
    int A,B;
    std::cin >> A >> B;
    std::cout << (A+B)%24 << '\n';
    return 0;
}
