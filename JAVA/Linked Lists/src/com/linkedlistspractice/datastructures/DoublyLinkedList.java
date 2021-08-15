package com.linkedlistspractice.datastructures;

@SuppressWarnings("ALL")
public class DoublyLinkedList {

    public Node head = null;
    public Node tail = null;
    public int size = 0;

    public void printlist(){
        System.out.println("===========This is a Doubly linked list===============");
        Node traverse_front = head;
        while(traverse_front != null){
            System.out.println(traverse_front.data + "->");
            traverse_front = traverse_front.next;
        }
        System.out.print("->");

        /**
         * now printing the doubly linked list from the back
         */
        Node traverse_back = tail;
        while(traverse_back != null){
            System.out.println(traverse_back.data + "->");
            traverse_back = traverse_back.prev;
        }
        System.out.print("null");

        /**
         * in the singly linked list we create a variable and make it point to the head and then
         * iterate through the list from the first element to the last
         * in doubly linked lists we do the same to traverse in from first element to the tail
         * and then as an addition we create a variable of type node and make it point to tail
         * and iterate back the linked list to get the exact same as the list we got before
         */
    }

    public Node getHead(){
        return head;
    }
    public Node getTail(){
        return tail;
    }

    public Node findNode(int element){
        /**
         * find node funtion returns the pointer to the node if the element is found and
         * if the element is not found it will return null
         */

        Node iterate = head;
        while(iterate != null){
            //if the element is found then return the pointer to that element
            if (iterate.data == element){
                return iterate;
            }
            //moving the pointer to  the next node
            iterate = iterate.next;
        }
        //returning null if the element in the linked list is not found
        return null;
    }

    public void insertFirst(int element){
        //creating the new node to insert here
        Node new_data = new Node(element);
        if(size == 0){
            /**
             * if size of the linked list is zero
             * then head and tail will br pointing the same element
             * and making the element of head as the element given will solve this
             * and making the head point to null using orevious pointer
             */
            head = tail;
            head.data = element;
            head.prev = null;
        }
        else{
            //making the new data point to the old head
            new_data.next = head;

            //making the new data as the new head
            head = new_data;

            //making the new data's previous pointer point to null
            new_data.prev = null;

            //making the next element of the new data point to newdata with a previous pointer
            new_data.next.prev = new_data;

            //increasing the size
            size = size + 1;
        }
    }

    public void insertLast(int element){
        //creating a node common to all the edge cases
        Node new_data = new Node(element);

        if (size == 0){
            /**
             * if size of the linked list is zero
             * then head and tail will br pointing the same element
             * and making the element of head as the element given will solve this
             * and making the head point to null using orevious pointer
             */

            head = tail;
            head.data = element;
            head.prev = null;
        }
        else{
            //making the next of the current tail point to the new node which is now going to be the tail
            tail.next = new_data;

            //making new_node's previous pointer point to the current tail
            new_data.prev = tail;

            //changing the tail as new_data
            tail = new_data;

            //incresing the size of the linked list
            size = size + 1;
        }
    }

    public void deleteLast(){
        if (size == 0){
            System.out.println("Linked List Empty Exception");
            return;
        }
        /**
         * if the size of the linked list is 1 we can directly delete the one existing node and the decrease the size.
         */
        else if (size == 1){
            head = tail = null;
            size = size - 1;
        }
        else{
            Node delete_node = tail;

            //the node before the tail point to null
            tail.prev.next = null;

            //changing the tail pointer to the tail.prev

            tail = tail.prev;

            //deleting the previous tail

            delete_node.prev = null;

            //decreasing the size of the linked list by 1

            size = size - 1;
        }
    }
    public void deleteFirst(){
        if (size == 1){
            System.out.println("Linked List Empty Exception");
            return;
        }
        else if(size == 1){
            head = tail = null;
            size = size - 1;
        }
        else{
            Node delete_node = head;

            //making the second node's previous pointer point to null

            head.next.prev = null;

            //chaning the second node as head

            head = head.next;

            //removing the pointer to make the previous head dangling

            delete_node.next = null;

            //decreasing the size of the linked list
            size = size - 1;
        }
    }

    public void insertAfter(int u ,int v){
        /**
         * The point to remember here is that we are inserting u after the node containing the element v
         */

        //first create a node which is common for all the boundary cases
        Node new_node = new Node(u);

        //calling the find node function to know if the element exists or not if it exists then to get the pointer to the element
        Node iterate = findNode(v);
        /**
         * edge case - 1 : if the element to insert after is tail that id equivalent to inserting at the end of the linked list
         * so we call the insert last function with the element u passed as arg.
         */
        if (iterate == tail){
            insertLast(u);
        }
        else if(iterate != null){
            /**
             * if the element is found in the list in the position other than the tail then we should have these additional steps
             * since inserting after iterate .
             */
            if (iterate.next != null){
                iterate.next.prev = new_node;
                new_node.next = iterate.next;
            }
            /**
             * this is a replicated code if the element is found at the tail.
             */
            iterate.next = new_node;
            new_node.prev = iterate;
            size = size + 1;
        }
        else{
            System.out.println("Element to insert after not found");
        }
    }

    public void insertBefore(int u, int v){
        /**
         * inserting the node with element u is before the node containing the element v
         */

        //first creating the node ehich is compulsion for all the steps
        Node new_node = new Node(v);

        //calling the find node to know if the element is present in the list if present returns the pointer to the element
        Node iterate = findNode(v);

        /**
         * edge case -1 : if the element to insert before is the head then this is equivalent to inserting at the begining of the linked list
         * so we call the insert First function passing the eleemnt u .
         */
        if (iterate == head){
            insertFirst(u);
        }
        /**
         * if the node containing the element is in the other position than the head then control reaches this else if clause.
         */
        else if(iterate != null){
            iterate.prev.next = new_node;
            new_node.next = iterate;
            new_node.prev = iterate.prev;
            new_node.next = iterate;
            size = size + 1;
        }
    }

    public void deleteAfter(int u){
        /**
         * edge case-1 : if the element is not found that is iterate == null then it should print following string
         * edge case-2 : if iterate is the second last element in the list then it should delete the tail in the list.
         * edge-case-3 : if the element to delete after is the tail itself then it shold just return.
         */

        //calling the find node function to find the elements pointer in the linked list
        Node iterate = findNode(u);

        if (iterate == null){
            System.out.println("Element to delete after not found");
        }
        //if the element found is the second last element
        else if (iterate.next == null){
            deleteLast();
        }
        //element is tail itself
        else if (iterate == tail){
            return;
        }
        else{
            //iterate.next pointer will be shifted to the iterate.next.next pointer
            /**
             *    1 <-> 2 <->3 <-> 4 <->5<-> null before that step
             */
            iterate.next = iterate.next.next;
            /**                   \         '\' shows that 2 is pointing to 4
             *    1 <-> 2 <-3 <-> 4 <->5<-> null before that step
             *    if the new iterate.next is also not null then the prev pointer of iterate.next should point iterate.
             */
            if (iterate.next != null){
                iterate.next.prev = iterate;
            }
            //decreasing the size of the linked list by 1
            size = size - 1;
        }
    }
    public void deleteBefore(int u){
        /**
         * edge case-1 : if the element is not found that is iterate == null then it should print following string
         * edge case-2 : if iterate is the second element in the list then it should delete the head in the list.
         * edge-case-3 : if the element to delete after is the head itself then it shold just return.
         */

        //calling the find node  function to find the pointer to the element u
        Node iterate = findNode(u);

        if (iterate == null){
            System.out.println("Element to delete before not found");
        }

        //if the element is the second element
        else if(iterate.prev == head){
            deleteFirst();
        }
        //if the element id the head itself
        else if(iterate == head ){
            return;
        }
        else{
            iterate.prev = iterate.prev.prev;
            if (iterate.prev != null){
                iterate.prev.next = iterate;
            }
            //decreasing the size by 1
            size = size - 1;
        }
    }
}
