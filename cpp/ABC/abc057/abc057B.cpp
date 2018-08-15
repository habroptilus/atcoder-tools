#include <iostream>
#include <cstdlib>
#include <cmath>

int get_distance(int a,int b,int c,int d){
    return std::abs(a-c)+std::abs(b-d);
}



int main(int argc, char const *argv[]) {
    int N,M;std::cin >> N>>M;
    int a[N],b[N];
    int c[M],d[M];

    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i]>>b[i];
    }
    for (size_t i = 0; i < M; i++) {
        std::cin >> c[i] >> d[i];
    }
    for (size_t i = 0; i < N; i++) {
        int min=std::pow(10,9);
        int min_j;
        for (size_t j = 0; j < M; j++) {
            int dist=get_distance(a[i],b[i],c[j],d[j]);
            if (dist<min) {
                min_j=j;
                min=dist;
            }
        }
        std::cout << min_j+1 << '\n';
    }

    return 0;
}
