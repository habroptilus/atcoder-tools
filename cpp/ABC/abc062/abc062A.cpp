#include <algorithm>
#include <iostream>
#include <vector>
int main(int argc, char const *argv[]) {
    int x, y;
    std::cin >> x >> y;
    std::vector<int> group{4, 6, 9, 11};
    auto xiter = std::find(group.begin(), group.end(), x);
    auto yiter = std::find(group.begin(), group.end(), y);
    if (x == 2 || y == 2) {
        std::cout << "No" << '\n';
    } else if (xiter != group.end() && yiter != group.end()) {
        std::cout << "Yes" << '\n';
    } else if (xiter == group.end() && yiter == group.end()) {
        std::cout << "Yes" << '\n';
    } else {
        std::cout << "No" << '\n';
    }

    return 0;
}
