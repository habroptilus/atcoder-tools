#include <iostream>

int main(int argc, char const *argv[]) {
    long long X;std::cin >> X;
    long long i=1;
    long long sum=0;
    while (true) {
        if (sum+i>=X) {
            std::cout << i << '\n';
            break;
        }
        sum+=i;
        i++;
    }
    return 0;
}
