# Data-Structures and Algorithms

Implementation of simple data structures in Python and c++ Mostly. (Java's work is still in progress)
_______

## Linked List

A singly linked list is made of nodes which contain a reference (or pointer) to the next node in the list and data. They are one of the simpliest data structures and can be used to implement other abstract data types including lists, stacks, queues etc.

![linked list](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

Advatange of a Linked list is a dynamic data structure which can grow while program is running (unlike arrays). Insertion and deletion methods are easy to implement, and it is a simple building block for other more complex data structures. 

The disadvantages of using a linked list is they use more memory than an array. Nodes must be read in order from the head to the tail (sequential access). Hard to reverse traverse a single linked list.

- **Implementation in Python :** [singly_linked_lists_actuall.py](https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/Python/singly_linked_lists_actuall.py)
- **Implementation in C++ :** [singly_linked_lists.cpp](https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/C%2B%2B/singly_linked_lists.cpp)


- **Resources:**
https://github.com/clair3st/Data-Structures

The list implementation supports the following methods:

___________________
| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **insertLast(val)**   | inserts the value in 'val' at the end of the linked list.  | O(n) (without tail pointer)          |
| **insertFirst(val)**      | inserts the value in 'val' at the beginning of the linked list (head). |   O(1)           |
| **deleteFirst()** | Deletes the first element of the linked list returns the element removed when called when the list is empty then 'ListEmptyException' | O(1)            |
| **deleteLast()** | Deletes the last node in the list      |    O(n)            |
| **PrintList()** | printlist function when called will print the linked list |    O(n)            |
| **findnode(val)** | This function when called returns the pointer to the node that has 'val' as an element in it. if the 'val' is not found in the linked list it returns Null. |    O(n)            |
| **getHead()** | returns the element that is in the head node.| O(1)|
| **isEmpty()** | returns a boolean true if the list is empty | O(1) |
| **getTail()** | returns the element in the last node (tail) | O(n) |
| **size()** | returns the size of the linked lists | O(1) |
| **delKth(val)**| deletes the kth element in the linked list| O(1) |
 ___________________

## Stack

A stack is a collection of nodes with operations occuring at one end only. It behaves like a real-world stack or pile of books - books can only be taken from  or placed on the top of the pile in a First In Last Out (LIFO) operations.

![stack](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/440px-Data_stack.svg.png)

-Stacks are handy for remembering state eg undo and redo
-Stacks can also be implemented using linked lists. 

- **Modules: ** 
	- **Python Implementation** [stack.py](https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/Python/stack.py)
	- **Python Implementation using linked lists** [stack_using_linked_lists.py](https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/Python/stack_using_linked_lists.py)
	- **C++ Implementation** [stacks.cpp](https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/C%2B%2B/stacks.cpp) 

- **Resources:**
https://github.com/clair3st/Data-Structures


The Stack implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **push(val)**   | inserts the 'val' at the top of the Stack  | O(1)           |
| **pop()**      |   deletes the top element of the stack and returns the same and if the stack is already empty returns 'StackEmptyException' |   O(1)        |
| **top()** | returns the top element in the stack without deleting it.| O(1)		|
|**isEmpty()**| returns true if the stack is empty else False | O(1)		|
|**printStack()**| This function will print space separated element in the stack. | O(n) |

_____________


## Double Linked List

A doubly linked list is made of nodes which contain a reference (or pointer) to the next node in the list, and the previous node in the list plus data. 

![doubly linked list](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

Advatange of a doubly linked list is two directional pointers allow traversal of the list in either direction.

The disadvantages of using a doubly linked list is they use more memory than a singly linked list and adding or removing a node requires changing more pointers.

- **Module: ** 

	-**Python Implementation** [doublylinkedlists.py] (https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/Python/doublylinkedlists.py)
	-**C++ Implementation** [Doublelinkedlist.cpp] (https://github.com/sridhar-5/Data-Structures-and-Algorithms/blob/main/Practice%20/C%2B%2B/Doublelinkedlist.cpp)

- **Resources:**
https://github.com/clair3st/Data-Structures

The list implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **insertLast(val)**   | inserts the value in 'val' at the end of the linked list.  | O(n) (without tail pointer)          |
| **insertFirst(val)**      | inserts the value in 'val' at the beginning of the linked list (head). |   O(1)           |
| **deleteFirst()** | Deletes the first element of the linked list returns the element removed when called when the list is empty then 'ListEmptyException' | O(1)            |
| **deleteLast()** | Deletes the last node in the list      |    O(n)            |
| **PrintList()** | printlist function when called will print the linked list |    O(n)            |
| **findnode(val)** | This function when called returns the pointer to the node that has 'val' as an element in it. if the 'val' is not found in the linked list it returns Null. |    O(n)            |
| **getHead()** | returns the element that is in the head node.| O(1)|
| **isEmpty()** | returns a boolean true if the list is empty | O(1) |
| **getTail()** | returns the element in the last node (tail) | O(n) |
| **size()** | returns the size of the linked lists | O(1) |
|**insertBefore(u,v)**| insert a node with value u before the node containing value v | O(1) |
|**insertAfter(u,v)** |  insert a node with value u after the node containing value v| O(1) |
|**deleteAfter(u)** |   delete the node after the node containting value u | O(1) |
|**deleteBefore(u)**|  delete the node before the node containting value u | O(1) | 
|**swap(u,v)**| swaps nodes containing elements u and v | O(n)|


_____________


## Queue

A queue is an ordered collection of nodes with operations only allowing the addition of new nodes to the tail and removing nodes from the head of the collection. The Queue is called a First In First Out (FIFO) data structure for this reason. 

<img alt="Queue" align="middle" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png" width="500">

Queues are used in computer science exactly like they are in the physical world, that is, they are a buffer and store data until it will later get processed. They have limited access (only insert at the tail) and they can always be added to (the length is unlimited).


- **Resources:**
https://github.com/clair3st/Data-Structures

The Queue implementation supports the following methods:


_____________

## Binary Search Tree

Binary Search Tree (BST) is a data structure used to map from key to value. A binary search tree relies on the property that keys that are less than the parent are found in the left subtree, and keys that are greater than the parent are found in the right subtree.

If the tree is empty, then a new node inserted into the tree becomes the tree’s root. The next node inserted will have its key compared to the key of the root node. If lower, it will occupy the “left” attribute of the root node. If higher, it occupies the “right” attribute. If a node tries to occupy the “left” or “right” attribute of the root and that attribute is already occupied, it moves down the tree to that node and has its key compared again.

![Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png) 

Binary Search Trees are a popular data structure choice in computing because of its efficient sorting and searching of data. On average, each comparison allows searching to ignore half of the tree. As such, each search takes time proportional to the logarithm of the number of items stored in the tree.


- **Resources:**
https://github.com/clair3st/Data-Structures

**Tree traversals**

This is the process of visiting each node in the tree once. Trees may be traversed in multiple ways so the output of nodes depends on the method used.

 - Depth first Traversals:
    - Pre-order traversal: F, B, A, D, C, E, G, I, H. <br>
    ![Pre-order](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Sorted_binary_tree_preorder.svg/440px-Sorted_binary_tree_preorder.svg.png)
    - In-order traversal: A, B, C, D, E, F, G, H, I. <br>
    ![In-order](https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sorted_binary_tree_inorder.svg/440px-Sorted_binary_tree_inorder.svg.png)
    - Post-order traversal: A, C, E, D, B, H, I, G, F. <br>
    ![Post-order](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Sorted_binary_tree_postorder.svg/440px-Sorted_binary_tree_postorder.svg.png)
- Breadth first Traversal:
    - Level-order: F, B, G, A, D, I, C, E, H. <br>
    ![Level-order](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Sorted_binary_tree_breadth-first_traversal.svg/440px-Sorted_binary_tree_breadth-first_traversal.svg.png)
