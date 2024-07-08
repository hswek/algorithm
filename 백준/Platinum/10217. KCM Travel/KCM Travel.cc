#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

const int INF = 99999999;

struct Node {
    int distance;
    int cost;
    int where;
    bool operator>(const Node& other) const {
        return distance > other.distance;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;

        vector<vector<pair<int, pair<int, int>>>> arr(103);

        for (int i = 0; i < k; ++i) {
            int u, v, cost, distance;
            cin >> u >> v >> cost >> distance;
            if (cost <= m) {
                arr[u].push_back(make_pair(distance, make_pair(cost, v)));
            }
        }

        queue<pair< pair<int,int>,int >> d;
        d.push(make_pair(make_pair(0,0),1));

        vector<vector<int>> m_list(103, vector<int>(10002, INF));
        m_list[1][0] = 0;

        while (!d.empty()) {
            
            

            int distance = -d.front().first.first;
            int cost = -d.front().first.second;
            int where = d.front().second;
            d.pop();
            if(m_list[where][cost] < distance)    continue;
            for (const auto& next : arr[where]) {
                int next_distance = next.first+distance;
                int next_cost = cost+next.second.first;
                int next_where = next.second.second;

                if (next_cost > m) continue;

                if (m_list[next_where][ next_cost] >  next_distance) {
                    for(int i=next_cost; i<=m;i++){
                        if (m_list[next_where][i] < next_distance) break;
                        m_list[next_where][i] = next_distance;
                    }
                    d.push(make_pair(make_pair(-next_distance,-next_cost),next_where));
                }
            }
        }

        int result = INF;
        for (int i = 0; i <= m; ++i) {
            result = min(result, m_list[n][i]);
        }

        if (result == INF) {
            cout << "Poor KCM\n";
        } else {
            cout << result << "\n";
        }
    }

    return 0;
}
