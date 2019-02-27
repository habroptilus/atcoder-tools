#include <bits/stdc++.h>
typedef long long ll;

std::vector<ll> str2num(std::string A) {
    std::map<char, ll> m;
    ll count = 0;
    std::vector<ll> ans;
    for (size_t i = 0; i < A.size(); i++) {
        auto itr = m.find(A[i]);
        if (itr != m.end()) {
            ans.push_back(itr->second);
        } else {
            ans.push_back(count);
            m[A[i]] = count;
            count++;
        }
    }
    return ans;
}

int main(int argc, char const *argv[]) {
    std::string S, T;
    std::cin >> S >> T;
    bool flag = true;

    for (size_t i = 0; i < S.size(); i++) {
        if (str2num(S)[i] != str2num(T)[i]) {
            flag = false;
        }
    }
    if (flag) {
        std::cout << "Yes" << '\n';
    } else {
        std::cout << "No" << '\n';
    }
    return 0;
}
