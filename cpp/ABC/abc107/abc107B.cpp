#include <iostream>
#include <string>
#include <vector>

void print(std::vector<std::string> v) {
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v[i] << '\n';
    }
}

int main(int argc, char const *argv[]) {
    int H, W;
    std::cin >> H >> W;
    std::string white_row(W, '.');
    std::string input_str;
    std::vector<std::string> grid;
    for (size_t i = 0; i < H; i++) {
        std::cin >> input_str;
        if (input_str != white_row) {
            grid.push_back(input_str);
        }
    }

    for (int i = W - 1; i >= 0; i--) {
        bool flag = true;
        for (size_t j = 0; j < grid.size(); j++) {
            if (grid[j][i] == '#') {
                flag = false;
                break;
            }
        }
        if (flag) {
            for (size_t k = 0; k < grid.size(); k++) {
                grid[k].erase(i, 1);
            }
        }
    }
    print(grid);
    return 0;
}
