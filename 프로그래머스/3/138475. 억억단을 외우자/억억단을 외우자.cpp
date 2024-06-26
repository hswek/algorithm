#include <string>
#include <vector>
#include <iostream>
using namespace std;
/*#def solution(e, starts):
#    answer = []
#    arr=[0]*(e+1)
#    for i in range(2,e+1):
#        for j in range(i,e+1,i):
#            arr[j]+=1
#    #print(arr)
#    return answer*/
vector<int> solution(int e, vector<int> starts) {
    vector<int> answer;
    int *arr=new int[e+1];
    
    for(auto i=0;i<=e;i++){
        arr[i]=0;
    }
    for( int i=2;i<=e;i++)
    {
        for(int j=i;j<=e;j+=i)
        {
            arr[j]+=1;
        }
    }

    int max_i=-1;
    int max_num=-1;
    for(int i=e;i>=1;i--)
    {
        if (max_num<=arr[i]){
            max_num=arr[i];
            max_i=i;
        }
        arr[i]=max_i;
    }
    for(int i=0;i<starts.size();i++)
    {
        answer.push_back(arr[starts[i]]);
}
    return answer;
}