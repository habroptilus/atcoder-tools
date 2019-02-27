#include <iostream>
#include <string>
#include <map>
int main(int argc, char const *argv[]) {
    int n;std::cin >> n;
    std::string S;
    std::map<char, int> outer_counter,inner_counter;

    std::string alphabet="abcdefghijklmnopqrstuvwxyz";

    for (size_t i = 0; i < alphabet.size(); i++) {
        inner_counter[alphabet[i]]=0;
        outer_counter[alphabet[i]]=10000;
    }
    for (size_t i = 0; i < n; i++) {
        std::cin >> S;
        for (size_t i = 0; i < S.size(); i++) {
            inner_counter[S[i]]+=1;
        }
        for (size_t i = 0; i < alphabet.size(); i++) {
            outer_counter[alphabet[i]]=std::min(outer_counter[alphabet[i]],inner_counter[alphabet[i]]);
            inner_counter[alphabet[i]]=0;
        }
    }

    for (size_t i = 0; i < alphabet.size(); i++) {
        if (outer_counter[alphabet[i]]!=0) {
            for (size_t j = 0; j < outer_counter[alphabet[i]]; j++) {
                std::cout << alphabet[i];
            }
        }
    }
    std::cout << '\n';
    return 0;
}
