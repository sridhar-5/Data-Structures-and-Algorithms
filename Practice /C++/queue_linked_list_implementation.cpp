#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>

using namespace std;

template<class E>
class QueueLL {
    public:
    class LinkedList{

        class Node{
            public:
            int data;
            Node* next;

            Node(int value){
                data = value;
                next = NULL;
            }
        };

        public:
        Node* first;
        Node* last;
        int sz;

        LinkedList(){
            first = last = NULL;
            sz = 0;
        }

        void empty_queue(E elt)
        {
            Node* new_node = new Node(elt);
            last = new_node;
            first = last;
            new_node->next = NULL;
            sz = sz + 1;
        }

        void non_empty_queue(E elt){
            Node* new_node = new Node(elt);
            last->next = new_node;
            last = new_node;
            new_node->next = NULL;
            sz = sz + 1;
        }
        
        E dequeue_empty(){

            E a = first->data;
            first->data = NULL;
            last = first;
            sz--;
            return a;
        }

        E dequeue_non_empty(){
            Node *temp = first;
            E a = temp->data;
            first=first->next;
            temp=NULL;
            sz-=1;
            return a;
        }

        void display()
        {
            if (sz!=0) {
			Node *temp = first;
			while (temp != NULL) {
				cout << temp->data << " ";
				temp = temp->next;
			}
			cout << endl;
			return;
		}
		cout << "Queue empty" <<endl;
        }

        int front_list(){
            return first->data;
        }
    };

public:

    LinkedList list = LinkedList();

	int size(){
        return list.sz;  
	}

	bool isEmpty(){
        return (list.sz == 0);
	}

	void enqueue(E elt){
        
        
        if(isEmpty()){
            list.empty_queue(elt);    
        }
        else{

            list.non_empty_queue(elt);
            
        }
        return;
	}

	E dequeue(){

         if(isEmpty())
        {
            cout << "Queue Empty Exception" << endl;
        }

        else if(list.sz==1)
        {
            list.dequeue_empty();
        }
            
        else{
            list.dequeue_non_empty();
        }
    }

        
	E front(){

        if(size() == 0){
            cout << "Queue Empty Exception"  << endl;
            return NULL;
        }

        else{
            return list.front_list();
        }
		
	}


	void displayQueue(){

        list.display();
		
	}


};

void getInput(string const &inputStr,vector <string> &myOutput)
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

int main(){
	QueueLL<int> queue;
 	string noOfInputs,str;
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
 	        queue.displayQueue();
 	    }
 	    else if(trim(it[0]) == 'D'){
 	    	queue.dequeue();
 	        queue.displayQueue();
 	    }
 	    else if(trim(it[0]) == 'S'){
 	    	cout<<queue.size()<<endl;
 	    }
 	    else if(trim(it[0]) == 'F'){
 	    	cout<<queue.front()<<endl;
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