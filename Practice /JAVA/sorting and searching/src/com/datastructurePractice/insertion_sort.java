package com.datastructurePractice;

import java.util.Arrays;

public class insertion_sort {
    public int[] array;
    public insertion_sort(int[] array){
        this.array = array;
    }

    public void sort(){
        int i,j,n = array.length;
        for(i = 1;i < n;i++){
            int value = array[i];

            j = i - 1;

            while(j >= 0 && array[j] > value){
                array[j+1] = array[j];
                j = j - 1;
            }
            array[j+1] = value;
        }
    }
    public void printArray(){
        System.out.println("The array (insertion sort) : " + Arrays.toString(array));
    }
}

