#include<iostream>
#include<vector>
using namespace std;
vector<pair<int,int>> combination_vec;
int max_num=0;
int x,y;
int **arr;
int **is_ok;
int **tmp_arr;
int x_arr[4]={1,0,-1,0};
int y_arr[4]={0,-1,0,1};
void infect(int** arr,int now_x,int now_y)
{
    for(int i=0;i<4;i++)
    {
        int nx=now_x+x_arr[i];
        int ny=now_y+y_arr[i];
        if (nx<0 || ny<0 || nx>=x || ny>=y) continue;
        if (arr[nx][ny]==0)
        {arr[nx][ny]=2;
        is_ok[nx][ny]=1;
        infect(arr,nx,ny);}
    }
}
int bfs(int ** arr)
{
    for(int i=0; i<x;i++) 
    {
        for(int j=0; j<y;j++) 
        {
            is_ok[i][j]=0;
        }   
    }
    for(int i=0; i<x;i++) 
    {
        for(int j=0; j<y;j++) 
        {
            if (is_ok[i][j]==1) continue;
            if (arr[i][j]==2) {infect(arr,i,j);}
        }
    }
    int result=0;
    for(int i=0; i<x;i++) 
    {
        for(int j=0; j<y;j++) 
        {
            if (arr[i][j]==0) result+=1;
        }   
    }
    return result;
}
void combination(int start, int count, vector<pair<int,int>> &picked) {
    // k select
    int k=3;
    if (count == k) {
		//somthing
        for(int i=0; i<x;i++) 
        {
            for(int j=0; j<y;j++) 
            {
                tmp_arr[i][j]=arr[i][j];
            }   
        }

        tmp_arr[picked[0].first][picked[0].second]=1;
        tmp_arr[picked[1].first][picked[1].second]=1;
        tmp_arr[picked[2].first][picked[2].second]=1;

        int now=bfs(tmp_arr);
        if (now>max_num) max_num=now;

        return;
    }

    for (int i = start; i <combination_vec.size(); ++i) {
        picked.push_back(combination_vec[i]);
        combination(i+1,count+1, picked);
        picked.pop_back();
    }

}
int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0);
    cin>>x;
    cin>>y;
    arr=new int*[x];
    for(int i=0; i<x;i++) arr[i]=new int[y];
    tmp_arr=new int*[x];
    for(int i=0; i<x;i++) tmp_arr[i]=new int[y];
    is_ok=new int*[x];
    for(int i=0; i<x;i++) is_ok[i]=new int[y];
    for(int i=0; i<x;i++) 
    {
        for(int j=0; j<y;j++) 
        {
            cin>>arr[i][j];
            if (arr[i][j]==0)
            combination_vec.push_back(make_pair(i,j));
        }   
    }
    vector<pair<int,int>> temp;
    combination(0,0, temp);
    cout<<max_num;
}