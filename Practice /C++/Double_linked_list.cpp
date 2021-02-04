#include <iostream>
#include<string>

using namespace std;

template <class T>
class DLList {
protected:
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
        Node new_node = new Node(x);
        if(head == NULL){
            head = new_node;
            new_node->prev = NULL;
            tail = new_node;
            n++;
        }
        else{
            Node iterate = head;
            while(iterate->next != NULL){
                iterate = iterate->next;
            }

            iterate->next = new_node;
            new_node->prev = iterate;
            new_node->next = NULL;
			tail = new_node;
            n++;
            
        }
		//@end-editable@
		return true;
	}

	T insertFirst(T x) {
	    //@start-editable@
		Node new_node = new Node(x);

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
		if(head == null){
            cout << "Linked List Empty Exception";
        }
		else if(head->next == NULL){
            head = NULL;
            tail = NULL;
			n--;
        }
        else{
            Node deleted = tail->prev->next;
            tail->prev->next = NULL;
			tail = deleted->prev;
            free(deleted);
			n--;
        }
		//@end-editable@
		return x;
		
	}

	T deleteFirst() {
	    //@start-editable@
		if(head == NULL){
            cout << "Linked List Empty Exception";
        }
        else if(head->next = NULL){
            head = NULL;
            tail = NULL;
			n--;
        }
		else{
            Node deleted = head;
            head = head->next;
            free(deleted);
			n--;
        }
		//@end-editable@
		return x;
	}

	//insert a node with value u after the node containing value v
    T insertAfter(T u,T v){
		Node inserted_this = new Node(u);
		Node iterate = head;
		while(iterate->next != NULL){
			if(iterate->element == v){
				break;
			}
			iterate = iterate->next;
		}
		Node temporary = iterate->next;
		temporary->prev = inserted_this;
		iterate->next = inserted_this;
		n++;
    	return true;
    }
    

    //insert a node with value u before the node containing value v

    T insertBefore(T u,T v){
		Node inserted_this = new Node(u);
		Node iterate = head;
		while(iterate->next != NULL){
			if(iterate->element == v){
				break;
			}
			iterate = iterate->next;
		}
		if(iterate->next == NULL){
			return;
		}
		else{
			iterate = iterate->prev;
			iterate->next = inserted_this;
			iterate = inserted_this;
			n++;
		}
    }

    //delete the node after the node containting value u
    T deleteAfter(T u){
		Node iterate = head;
		while(iterate->next !=NULL){
			if(iterate->element == u){
				break;
			}
			iterate = iterate->next;
		}
		if(iterate->next == NULL){
			return;
		}
		else{
			Node deleted_node = iterate->next;
			Node temp = iterate->next->next;
			iterate->next = iterate->next->next;
			temp->prev = iterate;
			free(deleted_node);
			n--;
		}
    }
    
	//delete the node before the node containting value u
    T deleteBefore(T u){
		Node iterate = head;
		while(iterate->next != NULL){
			if(iterate->element == u){
				break;
			}
			iterate = iterate->next;
		}
		if(iterate->next == NULL){
			return;
		}
		else{
			Node deleted_node = iterate->prev;
			Node temp = iterate->prev->prev;
			iterate->prev = iterate->prev->prev;
			temp->next = iterate;
			free(deleted_node);
			n--;
		}
    }

    Node findNode(T val){
		Node iterate = head;
		while(iterate->next != NULL){
			if(iterate->element == val){
				int temp = iterate->element;
			}
		}
		if(iterate->next == NULL){
			int temp = 0;
		}
    	return temp;
    }

    //swap the nodes containing u and v
    void swap(T u,T v){
		Node iterate_1 = head;
		while(iterate_1->next = NULL){
			if(iterate_1->element == u){
				break;
			}
			iterate_1 = iterate_1->next;
		}
		Node iterate_2 = head;
		while(iterate_2 != NULL){
			if(iterate_2->element = v){
				break;
			}
			iterate_2 = iterate_2->next;
		}
		int temp = iterate_1->element;
		iterate_1->element = iterate_2->element;
		iterate_2->element = temp;
    	return true;
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
			Node *temp = tail;
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

//Driver Code
int main(){
	DLList<int> dlist1;
 	string noOfInputs,str;
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str); 
 	    
 	    if (str.substr(0, 2) == "IF"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.insertFirst(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IL"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.insertLast(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DF"){
 	        dlist1.removeFirst();
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DL"){
 	        dlist1.removeLast();
 	        dlist1.printlist();
 	    }
 	    if (str.substr(0, 2) == "IA"){
 	        int value1 = stoi(str.substr(3, 5));
 	        int value2 = stoi(str.substr(6, 8));
 	        dlist1.insertAfter(value1,value2);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IB"){
 	        int value1 = stoi(str.substr(3, 5));
 	        int value2 = stoi(str.substr(6, 8));
 	        dlist1.insertBefore(value1,value2);
 	        dlist1.printlist();
 	    }
		if (str.substr(0, 2) == "DA"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.deleteAfter(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DB"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.deleteBefore(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "S"){
 	       cout<< dlist1.size()<<endl;
 	    }
 	    else if (str.substr(0, 1) == "F"){
 	       cout<< dlist1->head->element<<endl;
 	    }
 	    else if (str.substr(0, 1) == "L"){
 	       cout<< dlist1->tail->element<<endl;
 	    }
 	    else if (str.substr(0, 4) == "FIND"){
 	       int value1 = stoi(str.substr(5, 7));
 	       Node *temp = dlist1.findNode(value1)
 	       cout<<temp->element<<endl;
 	    }
 	    else if (str.substr(0, 2) == "SW"){
 	       int value1 = stoi(str.substr(3, 5));
 	       int value2 = stoi(str.substr(6, 8));
 	       dlist1.swap(value1,value2);
 	       dlist1.printlist();
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