#include <bits/stdc++.h>
typedef long long ll;
int main(int argc, char const *argv[]) {

    std::string S;
    std::cin >> S;
    ll ans = 0;
    ll add;
    int n = S.size() - 1;

    for (int bit = 0; bit < (1 << n); ++bit) {

        std::vector<int> partition_list;
        for (int i = 0; i < n; ++i) {
            if (bit & (1 << i)) { // i が bit に入るかどうか
                partition_list.push_back(i);
            }
        }
        int start = 0;
        std::string substr;
        // std::cout << "bit" << bit << '\n';
        for (int i = 0; i < partition_list.size(); ++i) {
            substr = S.substr(start, partition_list[i] - start + 1);
            start = partition_list[i] + 1;
            add = std::atol(substr.c_str());
            ans += add;
            // std::cout << add << '\n';
        }
        substr = S.substr(start, S.size() - start + 1);
        add = std::atol(substr.c_str());
        // std::cout << add << '\n';
        ans += add;
    }
    std::cout << ans << '\n';

    return 0;
}
