#include <iostream>

using namespace std;

class Node{
public:
  int data;
  Node* next;

  //constructor to initialize the data in the pointer

  Node(int data){
    this->data = data;
  }
};

void printlist(Node* n){
  while(n != NULL){
    cout << n->data;
    n = n-> next;
  }
}
int main(){
  Node* head = new Node(1);
  Node* second = new Node(2);
  Node* third = new Node(3);

  head->next = second;
  second->next = third;
  third->next = NULL;

  printlist(head);

  return 0;
}
