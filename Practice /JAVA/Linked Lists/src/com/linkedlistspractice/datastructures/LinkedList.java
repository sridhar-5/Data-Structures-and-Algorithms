package com.linkedlistspractice.datastructures;

import java.util.Stack;

@SuppressWarnings("ALL")
public class LinkedList {
    public Node head = null;
    public Node tail = null;


    //all the methods for the linked lists goes here
    public void printlist(){
        Node traverse = head;
        System.out.println("This is the current list : ");
        while(traverse != null) {
            System.out.print(traverse.data + "->");
            traverse = traverse.next;
        }
        System.out.print("null");
        System.out.println();
    }

    // all the ways of inserting a node goes here

    // inserting a node in the front of the list
    public void insertFirst(int new_data){
        //initializing a new node for the new element
        Node new_node = new Node(new_data);
        /**
         * since the new node should go in front of the current head so new_node.next = head
         * and since the first node is the new_node now head should be updated
         * so head = new_node
         */

        new_node.next = head;

        /**
         * moving the head to point to the new node
         */
        head = new_node;
    }
    //inserting the node after the given element
    public void insertAfter(Node previous_node,int new_data){

        //initializing the new_node with the given new_data
        Node new_node = new Node(new_data);
        /**
         * since this new element will go in the middle next element of the previous element
         * will be the next element to the new_node now
         *
         * and now since the new_node is pointing to the next node of the previous node
         *
         * now the next node of the previous node will be the current new_node
         */
        //making the new_node point to the previous.next node
        new_node.next = previous_node.next;

        //making the previous node point to the new_node

        previous_node.next = new_node;
    }
    //inserting the node at the end of the linked list
    public void insertLast(int new_data){

        //initializing the new node with the given data
        Node new_node = new Node(new_data);

        /**
         * since the new node should go in front of the current tail so new_node.next = tail
         * and since the last node node is the new_node now tail should be updated
         * so tail = new_node
         */

        /**
         * here threre is an additional case because if the list is empty then this node should
         * be made to be pointed by the head as well
         */
        if (head == null){
            head = new_node;
            return;
        }

        new_node.next = tail;
        /**
         * we should also make the node before the previous tail to point the tail now
         */
        Node last = head;
        //iterating to the last but one node and making it to point to the next element
        while(last.next != null){
            last = last.next;
        }
        last.next = new_node;
    }

    //Algorithm for the delete node is present here
    void delete_node(int value){
        Node temp = head;
        Node previous = null;

        /**
         * if the head node contains the value to be deleted then no need to search for
         * then no need to search and unlink the pointer right away
         */

        if(temp.data == value && temp != null){
            head = head.next;
            return;
        }

        /**
         * now if it is not the head node then we have to traverse through the linked list
         * and keep track of the iterating node as well as the previous node
         * so that we can update the prev node to the next node of the deleted node
         */

        while(temp != null && temp.data != value){
            previous = temp;
            temp = temp.next;
        }
        /**
         * there are two cases here as well
         * case-1:
         * if the value is found in the linked list
         * case-2:
         * if the value is found in the linked list then update the previous pointer and unlink
         * from the temp node
         */

        if(temp == null){
            return;
        }
        else{
            //unlinking the temp pointer
            previous.next = temp.next;
        }
    }

    public int getLengthOfLinkedList(){    //iterative method of getting the size of the linked list
        /**
         * Stratergy:
         * initializing the temp to 0
         * create a node pointer and make it point to the head of the linked list
         * let it traverse through the linked list and temp increment
         * and return count xD
         */
        Node temp = head;
        int count = 0;
        while(temp != null){
            temp = temp.next;
            count++;
        }
        return count;
    }

    public int getLength(){
        return getLengthRecursively(head);
    }
    public int getLengthRecursively(Node node){
        if(node == tail){
            return 0;
        }
        else{
            //incrementing the count and iterating if the node is not pointing the tail
            return 1 + getLengthRecursively(node.next);
        }
    }

    // this is an iterative process
    public boolean search(int value){
        Node curnode = head;

        /**
         * initializing the curnode to point to the head node and then traverse
         * if the curnode reached null pointer then return false else return true
         */

        while(curnode != null && curnode.data != value){
            curnode = curnode.next;
        }
        if (curnode != null){
            return true;
        }
        else{
            return false;
        }
    }

    //this is a recursive process
    public boolean searchRecursive(Node curnode,int x){
        /**
         * if the node is pointing to the tail we have to return false
         * and if the curnode.value == x then we should return true
         * else iterate to the next step
         */
        if(curnode == null){
            return false;
        }

        if(curnode.data == x){
            return true;
        }
        return searchRecursive(curnode.next,x);
    }

    //printting the middle element
    public void middle_element(){
        /**
         * here we make use of two pointers use the first pointer to iterate by step value 1 and
         * the second pointer will iterate with the step value 2 an and in this way when the second pointer which reaches the end
         * the slow pointer which is iterating by step 1 will reaching the middle element
         */
        Node pointer_one =head;
        Node pointer_two = head;

        if(head != null){
            while(pointer_one != null && pointer_two.next != null){
                pointer_one = pointer_one.next;
                pointer_two = pointer_two.next.next;
            }
            System.out.println("The middle element is :" +pointer_one.data);
        }
    }
    //find the number of occurences of an element in the node
    public int no_of_occurences(int val){
        int count = 0;
        /**
         * initialize the count to zero
         * and then traverse through the linked list and increment the count
         * once if you find the element and keep finding the element
         */
        Node search_pointer = head;
        while(search_pointer != null){
            if(search_pointer.data == val){
                count = count + 1;
            }
            search_pointer = search_pointer.next;
        }
        return count;
    }
    public boolean is_palindrome(){
        Node iterate = head;
        /**
         * strategy: to check this the smartest way is to use a stack of integers
         * we basically push all the data in the nodes into the stack and then
         * pop them out in order and check with the linked list again.
         */
        //initializing a stack of integer type here
        Stack<Integer> s = new Stack<Integer>();

        //first push all the elements into the stack
        while(iterate != null){
            s.push(iterate.data);
            iterate = iterate.next;
        }

        /**
         * now again start from the first and traverse through the linked list and check
         * with the top element in the stack and then while traversing pop the element to
         * check the next element and then continue to so till you reach the tail
         */

        boolean palin = true;

        iterate = head;
        while(iterate != null){
            int i = s.pop();

            if(iterate.data == i){
                palin = true;
            }
            else{
                palin = false;
                break;
            }
            iterate = iterate.next;
        }
        return palin;
    }

    //remove duplicates from a sorted linked lists
    public void remove_duplicates() {
        Node current_node = head;

        while (current_node != null) {
            Node tempor = current_node;

            while (tempor != null && tempor.data == current_node.data) {
                tempor = tempor.next;
            }
            //still about to complete a bit lazy............xD
        }
    }
}
