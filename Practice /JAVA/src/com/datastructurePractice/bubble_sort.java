package com.datastructurePractice;

import java.util.Arrays;

public class bubble_sort {
    public int[] array;
    public int count;

    //parametrized constructor
    public bubble_sort(int[] a){
        this.array = a;
    }

    //sorting algorithm starts here
    public void sort(){
        int n = array.length;
        for(int i = 0;i < n;i++){
            System.out.println(Arrays.toString(array));
            for(int j = 0;j < n - 1 -i;j++){
                if(array[j] > array[j+1]){
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    //printing array here
    public void printArray(){
        System.out.println("The Array : " + Arrays.toString(array));
    }
}
