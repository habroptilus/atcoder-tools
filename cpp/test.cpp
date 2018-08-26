#include <algorithm>
#include <iostream>
#include <vector>

typedef std::pair<int, int> pair;

void print(std::vector<pair> x) {
    std::cout << "[";
    for (size_t i = 0; i < x.size(); i++) {
        std::cout << "(" << x[i].first << ", " << x[i].second << ")";
        if (i != x.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << '\n';
}

bool compare_second(pair p1, pair p2) { return p1.second < p2.second; }

int main(int argc, char const *argv[]) {
    for (size_t i = 10; i >= 1; i--) {
        std::cout << i << '\n';
    }
    size_t h = -1;
    std::cout << h << '\n';
    return 0;
}
