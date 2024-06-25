#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
bool visit[32001];
vector<int> vec[32001];
void dfs(int node)
{
    if (visit[node]==true) return;
    for(int i:vec[node])
    {
        if(!visit[i])
        {
            dfs(i);
        }
    }
    visit[node]=true;
    cout<<node<<" ";
}
int main()
{
    int n,m;
    cin >> n >> m;
    int arr[n];
    for(int i=0;i<m;i++)
    {
        int x,y;
        cin >>x>>y;
        vec[y].push_back(x);
    }
    queue<int> q;
    for(int i=1;i<n+1;i++)
    {
        if (vec[i].empty()) {cout << i <<" "; visit[i]=true;}
        else q.push(i);
    }

    while (!q.empty())
    {
        int node= q.front();
        q.pop();
        if (visit[node]) continue;
        else dfs(node);
    }

}