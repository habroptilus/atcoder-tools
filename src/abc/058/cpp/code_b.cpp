#include <iostream>
#include <string>
int main(int argc, char const *argv[]) {
    std::string even,odd;
    std::cin >> odd >> even;
    int total=odd.size()+even.size();
    for (size_t i = 0; i < total; i++) {
        if (i%2==0) {
            std::cout << odd[i/2];
        }else{
            std::cout << even[(i-1)/2];
        }
    }
    std::cout << '\n';
    return 0;
}
