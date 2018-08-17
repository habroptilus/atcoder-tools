#include <iostream>

int main(int argc, char const *argv[]) {
    int W,a,b;
    std::cin >> W>>a>>b;
    if (b+W<a) {
        std::cout << a-b-W << '\n';
    }else if(a+W<b){
        std::cout << b-a-W << '\n';
    }else{
        std::cout << 0 << '\n';
    }
    return 0;
}
