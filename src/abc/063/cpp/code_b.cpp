#include <iostream>
#include <string>
int main(int argc, char const *argv[]) {
    std::string s;
    std::cin >> s;
    bool flag=true;
    for (size_t i = 0; i < s.size(); i++) {
        std::string sub=s.substr(i+1,s.size()-i);
        if (sub.find(s[i])!=-1) {
            std::cout << "no" << '\n';
            flag=false;
            break;
        }
    }
    if (flag) {
        std::cout << "yes "<< '\n';
    }
    return 0;
}
