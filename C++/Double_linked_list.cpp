#include <iostream>
#include<string>
#include <sstream>
using namespace std;

template<class T>
class DLList {
public:
	class Node {
	public:
		T element;
		Node *next;
		Node *prev;
		Node(T x) {
		    //@start-editable@

			element = x;
            next = NULL;
            prev = NULL;
			
			
			//@end-editable@
		}
	};
	Node *head;
	Node *tail;
	int n;
public:
	DLList() {
		n = 0;
		head = tail = NULL;
	}

	bool isEmpty(){
		//@start-editable@

		return n==0;		

		
		//@end-editable@
	}

	int size() {
	    //@start-editable@

	    return n;
	    
	    //@end-editable@
	}

	bool insertLast(T x) {
	    //@start-editable@

		
	    Node *new_node = new Node(x);
        if(head == NULL){
            head = new_node;
            new_node->prev = NULL;
            tail = new_node;
            n++;
        }
        else{

			tail->next = new_node;
			new_node->prev = tail;
			tail = new_node;
			new_node->next = NULL;
			n++;
        }	
		
		
		
		//@end-editable@
		return true;
	}

	T insertFirst(T x) {
	    //@start-editable@

		
		Node *new_node = new Node(x);

        if(head != NULL){
            new_node->next = head;
            new_node->prev = NULL;
            head->prev = new_node;
            head = new_node;
            n++;
        }
        else{
            new_node->next = head;
            new_node->prev = NULL;
            head = new_node;
			tail = new_node;
            n++;
        }    
		
		
		
		//@end-editable@
		return x;
	}

	T deleteLast() {
	    //@start-editable@

		
		if(isEmpty()){
            cout << "List Empty" << endl;
        }
		else if(n == 1){
            head = NULL;
            tail = NULL;
			n = 0;
        }
        else{
            Node *deleted = tail;
			tail = tail->prev;
			deleted->prev = NULL;
			tail->next = NULL;
            free(deleted);
			n--;
        }
        int x = 0;
 		
		
		
		//@end-editable@
		return x;
		
		
	}

	T deleteFirst() {
	    //@start-editable@

		
		if(isEmpty()){
            cout << "List Empty" <<endl;
        }
        else if(n == 1){
            head = NULL;
            tail = NULL;
			n = 0;
        }
		else{
            Node *deleted = head;
            head = head->next;
			head->prev = NULL;
            free(deleted);
			n--;
		}
		int x = 0;
		
		
		
		
		//@end-editable@
		return x;
	}

	//insert a node with value u after the node containing value v
    T insertAfter(T u,T v){
    	//@start-editable@

		
		Node *inserted_this = new Node(u);
		Node *iterate = findNode(v);
		
		if(iterate == tail){
			insertLast(u);
		}
		else if(iterate != NULL){
			if(iterate->next != NULL){
				iterate->next->prev = inserted_this;
				inserted_this->next = iterate->next;
			}
			inserted_this->prev = iterate;
			iterate->next = inserted_this;
			n++;
		}
		else{
			cout << "Node to insert after not found\n";
		}
		
		return u;
		
		//@end-editable@
    	return true;
    }
    

    //insert a node with value u before the node containing value v

    T insertBefore(T u,T v){
    	//@start-editable@

		
		Node *inserted_this = new Node(u);
		Node *iterate = findNode(v);
		if(iterate == head){
			insertFirst(u);
		}
		else if(iterate != NULL) {
			inserted_this->next = iterate;
			inserted_this->prev = iterate->prev;
			iterate->prev->next = inserted_this;
			iterate->prev = inserted_this;
			n++;
			
		}
		else{
			cout << "Node to insert before not found\n";
		}
		
	return u;
		
		//@end-editable@
    	return true;
    }

    //delete the node after the node containting value u
    T deleteAfter(T u){
    	//@start-editable@

		
    if (isEmpty() or (n == 1 and tail->element != u))
            cout << "Node to delete after not found\n";
        else if (tail->element == u);
        else if (tail->prev->element == u)
            deleteLast();
        else{
          Node* temp = tail->prev->prev;
            while (temp != NULL){
              if (temp->element == u){
                  
                    temp->next = temp->next->next;
                    temp->next->prev = temp;
                    n --;
                    return u;
            } 
        temp = temp->prev;
    } 
        cout << "Node to delete after not found\n";
    }
    return u;
    
		
		
		//@end-editable@

    }
    
	//delete the node before the node containting value u
    T deleteBefore(T u){
    	//@start-editable@

		

    if (isEmpty() or (n == 1 and head->element != u))
            cout << "Node to delete before not found\n";
        else if (head->element == u);
        else if (head->next->element == u)
            deleteFirst();
        else{
          Node* iterate = head->next->next;
            while (iterate != NULL){
              if (iterate->element == u){
                iterate->prev = iterate->prev->prev;
                    iterate->prev->next = iterate;
                    n --;
                    return u;
        } 
                iterate = iterate->next;
      }
           cout << "Node to delete before not found\n";
    }
    return u;
 		
		
		
		
		//@end-editable@

    }

    T getHead() {
    	//@start-editable@

		
    	return head->element;
		
		
		//@end-editable@

    }

    T getTail() {
    	//@start-editable@

		
		
     	return tail->element;
		
		
		
		//@end-editable@

    }

    Node* findNode(T val){
    	//@start-editable@

		
		if (isEmpty()){
			return NULL;
		}

		Node *iterate = head; 
		while(iterate != NULL){
			if(iterate->element == val){
				return iterate;
			}
			iterate = iterate->next;
		}
		return NULL;
		
		Node* temp = iterate;
		
		
		
		
		//@end-editable@
    	return temp;
    }

    //swap the nodes containing u and v
    void swap(T u,T v){
    	//@start-editable@

		Node *iterate_1 = head;
		while(iterate_1 != NULL){
			if(iterate_1->element == u){
				break;
			}
			iterate_1 = iterate_1->next;
		}
		Node *iterate_2 = head;
		while(iterate_2 != NULL){
			if(iterate_2->element == v){
				break;
			}
			iterate_2 = iterate_2->next;
		}
		int temp = iterate_1->element;
		iterate_1->element = iterate_2->element;
		iterate_2->element = temp;
		
		
		
		
		
		//@end-editable@

    	
    }
     
	//Prints the list
	void printlist(){
		if (!isEmpty()) {
			Node *temp = head;
			while (temp != NULL) {
				cout << temp->element << "->";
				temp = temp->next;
			}
			cout << endl;
			temp = tail;
			while (temp != NULL) {
				cout << temp->element << "->";
				temp = temp->prev;
			}
			cout << endl;
			return;
		}
		cout << ("Linked List Empty Exception")<<endl;
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
	DLList<int> dlist1;
 	string noOfInputs,str;
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str); 
 	    
 	    if (str.substr(0, 2) == "IF"){
 	        int value = getValue(str, 1);
 	        dlist1.insertFirst(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IL"){
 	        int value = getValue(str, 1);
 	        dlist1.insertLast(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DF"){
 	        dlist1.deleteFirst();
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DL"){
 	        dlist1.deleteLast();
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IA"){
 	        int value1 = getValue(str, 1);
 	        int value2 = getValue(str, 2);
 	        dlist1.insertAfter(value1,value2);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IB"){
 	        int value1 = getValue(str, 1);
 	        int value2 = getValue(str, 2);
 	        dlist1.insertBefore(value1,value2);
 	        dlist1.printlist();
 	    }
		else if (str.substr(0, 2) == "DA"){
 	        int value = getValue(str, 1);
 	        dlist1.deleteAfter(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DB"){
 	        int value = getValue(str, 1);
 	        dlist1.deleteBefore(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "L"){
 	       cout<< dlist1.getTail()<<endl;
 	    }
 	    else if (str.substr(0, 4) == "FIND"){
 	       int value1 = getValue(str, 1);
 	       DLList<int> :: Node *temp = dlist1.findNode(value1);
 	       if (temp!=NULL){
 	       	cout<<temp->element<<endl;
 	       }
 	       else{
 	       	cout<<"NULL"<<endl;
 	       }
 	    }
 	    else if (str.substr(0, 1) == "F"){
 	       cout<< dlist1.getHead()<<endl;
 	    }
 	    else if (str.substr(0, 2) == "SW"){
 	       int value1 = getValue(str, 1);
 	       int value2 = getValue(str, 2);
 	       dlist1.swap(value1,value2);
 	       dlist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "S"){
 	       cout<< dlist1.size()<<endl;
 	    }
 	    else if (str.substr(0,1) == "I"){
 	        //cout<<slist1.isEmpty()<<endl;
 	        if(dlist1.isEmpty()){
 	            cout<<"True"<<endl;
 	        }
 	        else{
 	            cout<<"False"<<endl;
 	        }
 	    }
 	}
}