package com.linkedlistspractice.datastructures;

@SuppressWarnings("ALL")
public class Main {
    public static void main(String[] args){
        LinkedList list = new LinkedList();
        Node first = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);

        //referencing the head here
        list.head = first;

        /**

        Three nodes have been created.
        We have references to these three blocks as head,
        second and third

                list.head        second              third
                   |                |                  |
                   |                |                  |
                +----+------+     +----+------+     +----+------+
                | 1  | None |     | 2  | None |     |  3 | None |
                +----+------+     +----+------+     +----+------+
       **/

        first.next = second; // link the first node to second

        /**

        Now next of first Node refers to second.  So they
        both are linked.

                  llist.head        second              third
                      |                |                  |
                      |                |                  |
                +----+------+     +----+------+     +----+------+
                | 1  |  o-------->| 2  | null |     |  3 | null |
                +----+------+     +----+------+     +----+------+
                        '''
       **/

        second.next = third; //link the second node to the third

        /**
            Now next of second Node refers to third.  So all three
            nodes are linked.

                llist.head        second              third
                    |                |                  |
                    |                |                  |
               +----+------+     +----+------+     +----+------+
               | 1  |  o-------->| 2  |  o-------->|  3 | null |
               +----+------+     +----+------+     +----+------+

         **/

    }
}
