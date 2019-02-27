#include <iostream>
#include <vector>
#include <algorithm>
int main(int argc, char const *argv[]) {
    long N,K;std::cin >> N >> K;
    typedef std::pair<long, long> pair;
    std::vector<pair> v;
    long a,b;
    for (size_t i = 0; i < N; i++) {
        std::cin >> a >> b;
        v.push_back(pair(a,b));
    }
    std::sort(v.begin(),v.end());
    long s=0;
    for (size_t i = 0; i < v.size(); i++) {
        if (s+v[i].second < K) {
            s+=v[i].second;
        }else{
            std::cout << v[i].first << '\n';
            break;
        }
    }

    return 0;
}
