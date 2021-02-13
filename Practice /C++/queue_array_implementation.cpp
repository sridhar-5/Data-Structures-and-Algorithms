#include<string>
#include<iostream>
#include <vector>
#include <sstream>
#include<iterator>
using namespace std;

template<class E>
class QueueArray {
private:
  int maxsize;
  int frnt;
  int rear;
  int arrSz;
  E *queue;

public:
  QueueArray(int sz){
    maxsize = sz;
    frnt = -1;
    rear = -1;
    arrSz = 0;
    queue = new E[maxsize];
    for(int i=0;i<sz;i++)
      queue[i] = NULL;
  }
  int size(){
    return arrSz;
  }

  bool isEmpty(){
    return arrSz == 0;
  }

  void enqueue(E elt){
    if(arrSz == maxsize){
      cout<<"Queue Full Exception\n";
      return;
    }
    rear = (rear+1)%maxsize;
    queue[rear] = elt;
    arrSz++;
    displayqueue();
  }

  E dequeue(){
    if(isEmpty()){
      cout<<"Queue Empty Exception\nNone\n";
      return -1;
    }
    frnt = (frnt+1)%maxsize;
    E temp = queue[frnt];
    queue[frnt] = NULL;
    arrSz--;
    return temp;
  }

  E first(){
    if(isEmpty()){
      cout<<"Queue Empty Exception\nNone\n";
      return -1;
    }
    return queue[(frnt+1)%maxsize];
  }

  void delk(E k){
    E ele;
    int sz = arrSz;
    for(int i=0;i<sz;i++){
      ele = dequeue();
      if(i == k-1){
        continue;
      }
      else
        enqueue(ele);
    }
  }
  void displayqueue(){
    if (isEmpty()){
      cout<< "Queue Empty\n";
    }
    else{
      for (int i=0;i<maxsize;i++){
        if (queue[i]!=NULL){
          cout<<queue[i]<<" ";
        }
      }
      cout << endl;
      return;
    }
  }
};

void getInput(string const &inputStr,vector<string> &myOutput)
{
    stringstream ss(inputStr);
    string st ="";
    while (getline(ss, st, ' ')) {
        myOutput.push_back(st);
    }
}
char trim(string str) 
{ 
   return str[0];
} 
//Driver Code
int main(){
  string noOfInputs,max,str;
  getline(cin, max);
   QueueArray<int> queue(stoi(max));
   getline(cin, noOfInputs);
   for(int i=0;i<stoi(noOfInputs);i++){
       vector<string> myOutput;
     str="";
       getline(cin, str); 
       getInput(str,myOutput);
       auto it = myOutput.begin();
        //Note:if there is a sequence expected beyond first char, then DO NOT use trim()
       if(it[0] == "E"){
         ++it;
         queue.enqueue(stoi(*it));
       }
       else if(it[0] == "DK"){
         ++it;
         queue.delk(stoi(*it));
         //queue.displayqueue();
       }
       else if(trim(it[0]) == 'D'){
         int temp=queue.dequeue();
         if(temp!=-1)
           cout<<temp<<endl;
           queue.displayqueue();
       }
       else if(trim(it[0]) == 'S'){
         cout<<queue.size()<<endl;
       }
       else if(trim(it[0]) == 'F'){
         int temp = queue.first();
         if(temp!=-1)
           cout<<temp<<endl;
       }
       else if(trim(it[0]) == 'I'){
         if(queue.isEmpty()){
             cout<<"True"<<endl;
         }
         else{
             cout<<"False"<<endl;
         }
       }
       else{
           cout<<"Invalid Input"<<endl;
       }
   }
}