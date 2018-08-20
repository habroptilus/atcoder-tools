#include <iostream>
#include <vector>
#include <algorithm>

typedef std::pair<int, int> pair;

void print(std::vector<pair> x){
    std::cout << "[";
    for (size_t i = 0; i < x.size(); i++) {
        std::cout << "(" << x[i].first<< ", " <<x[i].second << ")";
        if (i!=x.size()-1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << '\n';
}

bool compare_second(pair p1, pair p2){
    return p1.second < p2.second;
}

int main(int argc, char const *argv[]) {
    std::vector<pair> v;
    int a[5]={1,3,10,5,2};
    int b[5]={2,1,6,4,7};
    for (size_t i = 0; i < 5; i++) {
        v.push_back(pair(a[i],b[i]));
    }

    print(v);
    //std::sort(v.begin(),v.end(),compare_second);
    std::sort(v.begin(),v.end(),[](pair p1, pair p2){return p1.second < p2.second;});
    print(v);
    return 0;
}
