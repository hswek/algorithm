#include <iostream>
using namespace std;

int main(){
    int T, R, n;
    string S;
    cin>>T;
    for(int i=0; i<T; i++){
        cin>>R>>S;
        n=S.length();
        for(int k=0; k<n; k++){
            for(int j=0; j<R; j++)
            {
                cout<<S[k];
            }
        }
        cout<<"\n";
    }
}