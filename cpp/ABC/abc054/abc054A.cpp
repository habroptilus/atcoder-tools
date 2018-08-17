#include <iostream>

int main(int argc, char const *argv[]) {
    int A,B; std::cin >> A >> B;

    if (A==1) {
        A=14;
    }
    if (B==1) {
        B=14;
    }
    if (A>B) {
        std::cout << "Alice" << '\n';
    }else if(A<B){
        std::cout << "Bob" << '\n';
    }else{
        std::cout << "Draw" << '\n';
    }
    return 0;
}
