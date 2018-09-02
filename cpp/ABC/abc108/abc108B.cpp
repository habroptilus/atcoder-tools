#include <iostream>
int main(int argc, char const *argv[]) {
    int x_1, y_1, x_2, y_2;
    std::cin >> x_1 >> y_1 >> x_2 >> y_2;
    std::cout << x_2 + y_1 - y_2 << " ";
    std::cout << y_2 + x_2 - x_1 << " ";
    std::cout << x_1 + y_1 - y_2 << " ";
    std::cout << y_1 + x_2 - x_1 << '\n';
    return 0;
}
