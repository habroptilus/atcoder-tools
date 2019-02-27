#include <string>
#include <iostream>
#include <vector>
int main(int argc, char const *argv[]) {
    std::vector<std::string> v(3);
    std::string a,b,c;
    std::cin >> v[0]>>v[1]>>v[2];
    if (v[0].back()==v[1].front() && v[1].back()==v[2].front()) {
        std::cout << "YES" << '\n';
    }
    else{
        std::cout << "NO" << '\n';
    }
    return 0;
}
