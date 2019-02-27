#include <iostream>
#include <string>
#include <vector>

bool check(std::vector<std::string> A,std::vector<std::string> B,int x,int y){
    int m=B.size();
    for (size_t i = 0; i < m; i++) {
        for (size_t j = 0; j < m; j++) {
            if (A[x+i][y+j]!=B[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void print(std::vector<std::string> X){
    int n = X.size();
    for (size_t i = 0; i < n; i++) {
        std::cout << X[i] << '\n';
    }
}


int main(int argc, char const *argv[]) {
    int N,M; std::cin >> N >> M;
    std::vector<std::string> A(N);
    std::vector<std::string> B(M);
    char c;
    for (size_t i = 0; i < N; i++) {
        for (size_t j = 0; j < N; j++) {
            std::cin >> c;
            A[i]+=c;
        }
    }
    for (size_t i = 0; i < M; i++) {
        for (size_t j = 0; j < M; j++) {
            std::cin >> c;
            B[i]+=c;
        }
    }

    //print(A);
    //print(B);

    bool flag=false;
    for (size_t i = 0; i < N-M+1; i++) {
        for (size_t j = 0; j < N-M+1; j++) {
            if (check(A,B,i,j)){
                flag=true;
            }
        }
    }
    if (flag) {
        std::cout << "Yes" << '\n';
    }else{
        std::cout << "No" << '\n';
    }
    return 0;
}
