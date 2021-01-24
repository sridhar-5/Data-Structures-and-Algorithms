package com.datastructurePractice;

public class linear_search {
    public int[] search_array;
    public int element;

    //constructor parametrized
    public linear_search(int element, int[] a){
        this.element = element;
        this.search_array = a;
    }
    //default constructor
    public linear_search(){
        this.element = 0;
    }
    public int find_element(){
        int i,found = 0;
        for(i = 0;i < search_array.length;i++){
            if(element == search_array[i]) {
                found = i;
            }
        }
        return found;
    }
}
