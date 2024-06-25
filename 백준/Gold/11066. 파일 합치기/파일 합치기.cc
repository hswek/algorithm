#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

vector<vector<pair<int,int>>> cache(501, vector<pair<int,int>>(501, make_pair(-1,-1)));

pair<int,int> recursive(vector<int>& arr, int start, int end) {
    if (cache[start][end] != make_pair(-1,-1))
        return cache[start][end];
    if (start + 1 == end)
        return { arr[start], 0 };
    if (start + 2 == end)
        return { arr[start] + arr[start + 1], arr[start] + arr[start + 1] };
    int min_num = 98765432;
    pair<int,int> min_result;
    for (int i = start + 1; i < end; i++) {
        pair<int,int> first = recursive(arr, start, i);
        pair<int,int> second = recursive(arr, i, end);
        int tmp = first.first + first.second + second.first + second.second;
        if (tmp < min_num) {
            min_num = tmp;
            min_result = { first.first + second.first, min_num };
        }
    }
    cache[start][end] = min_result;
    return min_result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cache.clear();
        cache.resize(501, vector<pair<int,int>>(501, make_pair(-1,-1)));
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        pair<int,int> result = recursive(arr, 0, n);
        cout << result.second << endl;
    }
    return 0;
}
