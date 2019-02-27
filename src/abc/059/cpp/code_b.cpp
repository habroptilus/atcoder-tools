#include <iostream>
int main(int argc, char const *argv[]) {
    std::string A,B;
    std::cin >> A>>B;
    bool flag=false;
    if (A.size()>B.size()) {
        std::cout << "GREATER" << '\n';
    }else if (A.size()<B.size()) {
        std::cout << "LESS" << '\n';
    }else{
        for (size_t i = 0; i < A.size(); i++) {
            if (A[i] > B[i]) {
                std::cout << "GREATER" << '\n';
                flag=true;
                break;
            }else if (A[i]<B[i]) {
                std::cout << "LESS" << '\n';
                flag=true;
                break;
            }
        }
        if (!flag) {
            std::cout << "EQUAL" << '\n';
        }
    }
    return 0;
}
