#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main(){
    int testcases;

    vector<int> s;
    vector<int> p;
    vector<int> v;
    vector<int> result;

    cin >> testcases;

    int x = 0;
    int n;
    while(x < testcases){

        cin >> n;
        for(int i = 0;i < n;i++){
            int temp_s,temp_p,temp_v;
            cin >> temp_s >> temp_p >> temp_v;
            s.push_back(temp_s);
            p.push_back(temp_p);
            v.push_back(temp_v);
        }    
        for(int i = 0;i < n;i++){
            int temp = floor(p[i]/(s[i]+1));
            temp = temp*v[i];
            result.push_back(temp);
        }

        cout << *max_element(result.begin(),result.end()) << endl; 
        s.clear();
        p.clear();
        v.clear();
        result.clear();     
        x = x + 1;
    }
    return 0;
}