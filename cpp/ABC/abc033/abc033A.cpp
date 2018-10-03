#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    std::string N;
    std::cin >> N;
    bool is_same = true;
    for (size_t i = 0; i < N.size(); i++) {
        if (N.front() != N[i]) {
            is_same = false;
        }
    }
    if (is_same) {
        std::cout << "SAME" << '\n';
    } else {
        std::cout << "DIFFERENT" << '\n';
    }
    return 0;
}
