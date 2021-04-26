package com.datastructurePractice;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("please enter the size of the array : ");
        int size_of_the_array = input.nextInt();
        int [] array = new int[size_of_the_array];
        System.out.println("input into array : ");
        for(int i = 0;i < size_of_the_array;i++){
            array[i] = input.nextInt();
        }
        System.out.println("element to be searched : ");
        int element_to_be_searched = input.nextInt();

        //creating an object that shows linear search
        linear_search s1 = new linear_search(element_to_be_searched,array);
        int index = s1.find_element();
        if(index > 0){
            System.out.println("The element is found at "+index);
        }
        else{
            System.out.println("Element not found");
        }

        //creating an object that implements binary_search
        binary_search b1 = new binary_search(element_to_be_searched,array);
        index = b1.find_element();
        if(index == -1){
            System.out.println("Not found");
        }
        else{
            System.out.println("The element found at "+index + " by binary search");
        }

        System.out.println("=====================searching section ends======================");

        System.out.println();

        //sorting section starts from here

        System.out.println("=================Learning Sorting Algorithms starts=================");

        int [] unsorted_array = {6,2,9,4,1};

        //selection sort object lies here
        selection_sort sort1 = new selection_sort(unsorted_array);
        sort1.sort();
        sort1.printArray();

        //bubble sort object lies here
         unsorted_array = new int[]{6, 2, 9, 4, 1};

        bubble_sort sort2 = new bubble_sort(unsorted_array);
        sort2.sort();
        sort2.printArray();

        //insertion sort object lies here
        unsorted_array = new int[]{6, 2, 9, 4, 1};

        insertion_sort sort3 = new insertion_sort(unsorted_array);
        sort3.sort();
        sort3.printArray();

        //merge sort object here
        unsorted_array = new int[]{6, 2, 9, 4, 1};
        int n = unsorted_array.length;
        Merge_sort sort4 = new Merge_sort();
        sort4.merge_sort(unsorted_array,0,n-1);
    }
}
