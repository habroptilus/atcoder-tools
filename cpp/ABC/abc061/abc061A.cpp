#include <iostream>
int main(int argc, char const *argv[]) {
    int A,B,C;
    std::cin >> A>>B>>C;
    if (A<=C && C<=B) {
        std::cout << "Yes" << '\n';
    }
    else{
        std::cout << "No" << '\n';
    }
    return 0;
}
