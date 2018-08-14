#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char const *argv[]) {
    std::string s1,s2,s3;
    std::cin >> s1 >> s2 >> s3;
    std::string t1{s1.front()};
    std::string t2{s2.front()};
    std::string t3{s3.front()};
    transform (t1.begin (), t1.end (), t1.begin (), toupper);
    transform (t2.begin (), t2.end (), t2.begin (), toupper);
    transform (t3.begin (), t3.end (), t3.begin (), toupper);
    std::cout << t1+t2+t3 << '\n';
    return 0;
}
