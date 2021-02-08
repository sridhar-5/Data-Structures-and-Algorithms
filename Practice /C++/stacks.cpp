#include <iostream>
#include<string>
#include <sstream>
using namespace std;

template<class T>
class StackArray {
private:
    int maxsize;
    int top;
    T *stack;

public:
    StackArray(int sz){
        maxsize = sz;
        top = -1;
        stack = new T[maxsize];
    }
    int size(){
      return top+1;
    }

    bool isEmpty(){
      bool x;
        if (top == -1){
            x = true;
            return x;
        }
        else{
          x = false;
          return x;
        }
        return x;    
    }

    void push(T& elt){
      if (size() >= maxsize){
        cout << "StackFullException";
        return ;
      }
      else{
        top = top + 1;
        stack[top] = elt;
      }
    }

    T pop(){
      if (isEmpty()){
        cout << "StackEmptyException"<<endl;
        return -1;
      }
      else{
        int x = stack[top];
        stack[top] = NULL;
        top = top - 1;
        return x;
      }
    }

    T Top(){
      if (isEmpty()){
        cout << "StackEmptyException"<<endl;
        return -1;
      }
      return stack[top];   
    }
    void printstack(){
        cout << endl;
        if (isEmpty()){
            cout<< "Empty";
        }
        else{
            for (int i=0;i<maxsize;i++){
                if (stack[i]!= NULL) {
                    cout<<stack[i]<<" ";
                }
            }
            cout << endl;
            return;
        }
    }
};

int getValue(string s, int pos) {
    istringstream iss(s);
    string temp;
    iss>>temp;
    iss>>temp;
    if(pos==1) {
        return stoi(temp);
    }
    else {
        iss>>temp;
        return stoi(temp);
    }
}
//Driver Code
int main(){
    string noOfInputs,max,str;
    getline(cin, max);
    StackArray<int> stack1(stoi(max));
    getline(cin, noOfInputs);
    for(int i=0;i<stoi(noOfInputs);i++){
        getline(cin, str); 
        
        if (str.substr(0, 1) == "S"){
           cout<< stack1.size()<<endl;
        }
        else if (str.substr(0,1) == "I"){
            //cout<<slist1.isEmpty()<<endl;
            if(stack1.isEmpty()){
                cout<<"True"<<endl;
            }
            else{
                cout<<"False"<<endl;
            }
        }
        else if (str.substr(0, 1) == "P"){
            int value = getValue(str, 1);
            stack1.push(value);
            stack1.printstack();
        }
        else if (str.substr(0, 1) == "O"){
            cout << stack1.pop();
            stack1.printstack();
        }
        else if (str.substr(0, 1) == "T"){
            cout << stack1.Top();
            stack1.printstack();
        }
        
    }
}
