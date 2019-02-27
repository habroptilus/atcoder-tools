#include <iostream>
#include <algorithm>
int main(int argc, char const *argv[]) {
    int N;std::cin >> N;
    int sum=0;
    int s;
    int min=10000;
    for (size_t i = 0; i < N; i++) {
        std::cin >> s ;
        sum+=s;
        if (s%10!=0 && s< min) {
            min=s;
        }
    }
    if (sum%10!=0) {
        std::cout << sum << '\n';
    }else if(min!=10000){
        std::cout << sum-min << '\n';
    }else{
        std::cout << 0 << '\n';
    }
    return 0;
}
