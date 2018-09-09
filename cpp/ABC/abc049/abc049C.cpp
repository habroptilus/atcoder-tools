#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    std::string S;
    std::cin >> S;
    std::reverse(S.begin(), S.end());

    while (!S.empty()) {
        if (S.substr(0, 6) == "resare") {
            S.erase(S.begin(), S.begin() + 6);
        } else if (S.substr(0, 7) == "remaerd") {
            S.erase(S.begin(), S.begin() + 7);
        } else if (S.substr(0, 5) == "maerd" || S.substr(0, 5) == "esare") {
            S.erase(S.begin(), S.begin() + 5);
        } else {
            std::cout << "NO" << '\n';
            return 0;
        }
    }
    std::cout << "YES" << '\n';
    return 0;
}
