#include <iostream>
#include <string>

int main(int argc, char const *argv[]) {
    std::string s;
    std::cin >> s;
    std::cout << s.rfind('Z')-s.find('A')+1 << '\n';
    return 0;
}
