#include<iostream>

template<class T>
class SLList{

   protected:
class Node{
public:
T element;
Node *next;
Node(T x){
element=x;next=NULL;}
};
Node *head;
Node *tail;
int sz;

public:
SLList()
{sz=0;
head=tail=NULL;}

bool isEmpty(){
return (sz==0);}
int size(){
return sz;}

T getHead(){
return head->x;
}


void InsertLast(T x){
Node *nnode = new Node(x);
if(isEmpty()){
hea=tail=nnode;
sz+=1;}
else{
tail->next=nnode;
tail=nnode;
sz+=1;
}
}

void insertFirst(T x){}

void remove First(){}

void remove Last(){}
}
