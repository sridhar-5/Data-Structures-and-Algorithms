package com.datastructurePractice;

public class binary_search {
    public int[] search_array;
    public int element;

    //constructor parametrized
    public binary_search(int element, int[] a){
        this.element = element;
        this.search_array = a;
    }

    public int find_element(){
        int length = search_array.length;
        int middle_element;
        //initially left and right boundaries are two corner elements in an array
        int left_boundary = 0;
        int right_boundary = length-1;
        int found = 0;

        while(right_boundary >= left_boundary){

            middle_element = left_boundary + (right_boundary-left_boundary)/2;

            if(search_array[middle_element] == element){
                found = 1;
                return middle_element;
            }

            if(search_array[middle_element] < element){
                left_boundary = middle_element+1;
            }
            if(search_array[middle_element] > element){
                right_boundary = middle_element - 1;
            }
        }
        return -1;
    }
}
