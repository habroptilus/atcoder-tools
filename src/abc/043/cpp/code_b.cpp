#include <bits/stdc++.h>
typedef long long ll;

int main(int argc, char const *argv[]) {
    std::string s;
    std::cin >> s;
    std::string ans;
    for (size_t i = 0; i < s.size(); i++) {
        if (s[i] == 'B') {
            if (!ans.empty()) {
                ans.pop_back();
            }
        } else {
            ans.push_back(s[i]);
        }
    }
    std::cout << ans << '\n';
    return 0;
}
