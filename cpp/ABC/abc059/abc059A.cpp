#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char const *argv[]) {
    std::string s1,s2,s3;
    std::cin >> s1 >> s2 >> s3;
    std::string s={s1.front(),s2.front(),s3.front()};
    transform(s.begin(),s.end(),s.begin(),toupper);
    std::cout << s << '\n';
    return 0;
}
