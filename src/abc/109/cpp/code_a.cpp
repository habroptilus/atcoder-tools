#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    int A, B;
    std::cin >> A >> B;
    if (A * B % 2 == 0) {
        std::cout << "No" << '\n';
    } else {
        std::cout << "Yes" << '\n';
    }
    return 0;
}
