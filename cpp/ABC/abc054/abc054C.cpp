#include <iostream>
#include <vector>

int search(int new_index, std::vector<int> *G, bool *visited, int N, int M) {

    bool finish = true;
    if (visited[new_index]) {
        return 0;
    }
    bool copied[N];
    for (size_t i = 0; i < N; i++) {
        copied[i] = visited[i];
    }

    copied[new_index] = true;
    for (size_t i = 0; i < M; i++) {
        if (!copied[i]) {
            finish = false;
            break;
        }
    }
    if (finish) {
        return 1;
    }
    int sum = 0;
    for (size_t i = 0; i < G[new_index].size(); i++) {
        sum += search(G[new_index][i], G, copied, N, M);
    }
    return sum;
}

int main(int argc, char const *argv[]) {
    int N, M;
    std::cin >> N >> M;
    std::vector<int> G[N];
    int a, b;
    bool visited[N];
    for (size_t i = 0; i < M; i++) {
        std::cin >> a >> b;
        G[a - 1].push_back(b - 1);
        G[b - 1].push_back(a - 1);
    }
    for (size_t i = 0; i < N; i++) {
        visited[i] = false;
    }

    std::cout << search(0, G, visited, N, M) << '\n';

    return 0;
}
