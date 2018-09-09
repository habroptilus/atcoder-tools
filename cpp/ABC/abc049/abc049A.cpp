#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    char c;
    std::cin >> c;
    std::vector<char> v = {'a', 'i', 'u', 'e', 'o'};
    for (size_t i = 0; i < v.size(); i++) {
        if (v[i] == c) {
            std::cout << "vowel" << '\n';
            return 0;
        }
    }
    std::cout << "consonant" << '\n';
    return 0;
}
