#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char const *argv[]) {
    std::string s1,s2,s3;
    std::cin >> s1 >> s2 >> s3;

    transform(s1.begin(),s1.end(),s1.begin(),toupper);
    transform(s2.begin(),s2.end(),s2.begin(),toupper);
    transform(s3.begin(),s3.end(),s3.begin(),toupper);
    std::cout << s1.front() << s2.front()<<s3.front()<<'\n';
    return 0;
}
