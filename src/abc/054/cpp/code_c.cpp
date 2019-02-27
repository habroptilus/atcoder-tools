#include <iostream>
#include <vector>
bool visited[8];
std::vector<int> G[8];
int N, M;

int search(int new_index) {
    bool finish = true;

    for (size_t i = 0; i < N; i++) {
        if (!visited[i]) {
            finish = false;
            break;
        }
    }
    if (finish) {
        return 1;
    }
    int sum = 0;
    for (size_t i = 0; i < G[new_index].size(); i++) {
        if (visited[G[new_index][i]]) {
            continue;
        }
        visited[G[new_index][i]] = true;
        sum += search(G[new_index][i]);
        visited[G[new_index][i]] = false;
    }
    return sum;
}

int main(int argc, char const *argv[]) {
    std::cin >> N >> M;
    int a, b;
    for (size_t i = 0; i < M; i++) {
        std::cin >> a >> b;
        G[a - 1].push_back(b - 1);
        G[b - 1].push_back(a - 1);
    }

    for (size_t i = 0; i < N; i++) {
        visited[i] = false;
    }
    visited[0] = true;
    std::cout << search(0) << '\n';

    return 0;
}
