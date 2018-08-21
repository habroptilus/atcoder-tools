#include <iostream>
#include <algorithm>

int main(int argc, char const *argv[]) {
    int N;std::cin >> N;
    long long a[N];
    for (size_t i = 0; i < N; i++) {
        std::cin >> a[i];
    }

    long long sum_1=0;
    long long ans_1=0;

    for (size_t i = 0; i < N; i++) {
        if (i%2==0 && sum_1+a[i] >= 0) {
            ans_1+=sum_1+a[i]+1;
            sum_1=-1;
        }else if(i%2==1 && sum_1+a[i] <= 0){
            ans_1+=1-sum_1-a[i];
            sum_1=1;
        }else{
            sum_1+=a[i];
        }
    }
    long long sum_2=0;
    long long ans_2=0;


    for (size_t i = 0; i < N; i++) {
        if (i%2==0 && sum_2+a[i] <= 0) {
            ans_2+=1-sum_2-a[i];
            sum_2=1;
        }else if(i%2==1 && sum_2+a[i] >= 0){
            ans_2+=sum_2+a[i]+1;
            sum_2=-1;
        }else{
            sum_2+=a[i];
        }
    }
    std::cout << std::min(ans_1,ans_2) << '\n';


    return 0;
}
