#include<iostream>

int arr[10001];
using namespace std;
void f(int start, int end)
{
    if (start==end-1) {cout<<arr[start]<<endl; return;}
    if (start>=end) return;

    int tmp=start+1;
    while(arr[tmp]<arr[start])
    {
        tmp++;
        if (tmp>=end) break;
    }
    f(start+1,tmp);
    f(tmp,end);
    cout << arr[start]<<endl;
    return;
}
int main()
{
    int num;
    int idx=0;
    while (cin >>num)
    {
        arr[idx]=num;
        idx++;
    }
    f(0,idx);


    return 0;
}   