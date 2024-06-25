#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    char word[101];
    cin>>word;
    int alphabet[26];
    for(int k=0; k<26; k++)
        alphabet[k]=-1;

    int i=0, index;
    while(1){
        if(word[i]=='\0')
            break;
        index=int(word[i])-97;
        if(alphabet[index]!=-1){
            i++;
            continue;
        }  
        alphabet[index]=i;
        i++;
    }
    for(int j=0; j<26; j++)
    {
        cout<<alphabet[j]<<" ";

    }
    return 0;
}