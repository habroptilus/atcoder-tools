#include <bits/stdc++.h>
typedef long long ll;

bool check(std::string &S, char &turn) {
    turn = S.front();
    S.erase(S.begin());
}

int main(int argc, char const *argv[]) {
    std::string A, B, C;
    std::cin >> A >> B >> C;
    char turn = 'a';
    while (true) {
        if (turn == 'a') {
            if (A.empty()) {
                std::cout << "A" << '\n';
                break;
            }
            check(A, turn);

        } else if (turn == 'b') {
            if (B.empty()) {
                std::cout << "B" << '\n';
                break;
            }
            check(B, turn);
        } else {
            if (C.empty()) {
                std::cout << "C" << '\n';
                break;
            }
            check(C, turn);
        }
    }
    return 0;
}
