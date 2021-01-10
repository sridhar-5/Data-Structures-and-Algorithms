package com.datastructurePractice;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("please enter the size of the array : ");
        int size_of_the_array = input.nextInt();
        int [] array = new int[size_of_the_array];
        for(int i = 0;i < size_of_the_array;i++){
            array[i] = input.nextInt();
        }
        int element_to_be_searched = input.nextInt();
        linear_search s1 = new linear_search(element_to_be_searched,array);
        int index = s1.find_element();
        if(index != 0){
            System.out.println("The element is found at "+index);
        }
        else{
            System.out.println("Element not found");
        }
    }
}
