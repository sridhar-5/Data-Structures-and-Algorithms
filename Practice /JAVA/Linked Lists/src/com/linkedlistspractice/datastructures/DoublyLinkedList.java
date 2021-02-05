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
        }
    }

}
