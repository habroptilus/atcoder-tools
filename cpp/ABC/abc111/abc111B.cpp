#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    ll N;
    std::cin >> N;
    ll x = N;
    bool flag;
    std::string str_x;
    while (true) {
        flag = true;
        str_x = std::to_string(x);
        for (size_t i = 0; i < str_x.size(); i++) {
            if (str_x[i] != str_x.back()) {
                flag = false;
                break;
            }
        }
        if (flag) {
            std::cout << x << '\n';
            break;
        }
        x++;
    }
    return 0;
}
