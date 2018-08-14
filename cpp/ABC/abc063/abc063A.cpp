#include <iostream>
int main(int argc, char const *argv[]) {
    int A;
    int B;
    std::cin >> A >> B;
    if (A+B>=10) {
        std::cout << "error" << '\n';
    }
    else{
        std::cout << A+B << '\n';
    }

    return 0;
}
