#include <bits/stdc++.h>
typedef long long ll;

bool find(std::vector<std::string> words, std::string w) {
    for (size_t i = 0; i < words.size(); i++) {
        if (words[i] == w) {
            return true;
        }
    }
    return false;
}

int main(int argc, char const *argv[]) {
    int N;
    std::cin >> N;
    std::string W[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> W[i];
    }
    std::vector<std::string> words;
    words.push_back(W[0]);
    for (size_t i = 1; i < N; i++) {
        if (find(words, W[i]) || W[i][0] != W[i - 1][W[i - 1].size() - 1]) {
            std::cout << "No" << '\n';
            return 0;
        }
        words.push_back(W[i]);
    }
    std::cout << "Yes" << '\n';
    return 0;
}
