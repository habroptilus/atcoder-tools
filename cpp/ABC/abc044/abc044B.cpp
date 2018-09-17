#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {
    std::string w;
    std::cin >> w;
    std::map<char, ll> counter;
    bool flag = true;
    for (size_t i = 0; i < w.size(); i++) {
        counter[w[i]] += 1;
    }
    for (auto item : counter) { // forもまわせる
        if (item.second % 2 != 0) {
            std::cout << "No" << '\n';
            flag = false;
            break;
        }
    }
    if (flag) {
        std::cout << "Yes" << '\n';
    }

    return 0;
}
