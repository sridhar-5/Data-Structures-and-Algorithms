package com.datastructurePractice;


import java.util.Arrays;

public class selection_sort {
    public int[] array;
    public int count = 0;

    //this is a parametrized constructor
    public selection_sort(int[] a){
        this.array = a;
    }

    //we implement swap and print array method separately to avoid clumsiness of the code

    public void sort(){
        int n = array.length;
        int minimum;
        for(int i = 0;i < n;i++){
            minimum = i;
            System.out.println(i+" th iteration "+Arrays.toString(array));
            for(int j = i+1;j < n;j++){
                count = count + 1;
                if(array[j] < array[minimum]){
                    minimum = j;
                }
            }
            //swapping the the two elements here
            int temp = array[i];
            array[i] = array[minimum];
            array[minimum] = temp;
        }
    }
    public void printArray(){
        System.out.println("The array :" + Arrays.toString(array));
        System.out.println(count);
    }
}
