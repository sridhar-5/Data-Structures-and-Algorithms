package com.datastructurePractice;

import java.util.Arrays;

public class Merge_sort {

    public void merge(int[] arr,int lower_boundary,int middle_ele,int upper_boundary){
        int i = lower_boundary;
        int j = middle_ele + 1;
        int k = lower_boundary;
        int[] array = new int[upper_boundary+1];

        while(i <= middle_ele && j <= upper_boundary){
            if(arr[i] < arr[j]){
                array[k] = arr[i];
                i = i + 1;
                k = k + 1;
            }
            else{
                array[k] = arr[j];
                j= j + 1;
                k = k + 1;
            }
        }
        //this additional lines of code is for the remaining elements if any
        if(i > middle_ele){
            while(j <= upper_boundary){
                array[k] = arr[j];
                j++;
                k++;
            }
        }
        else{
            while(i <= middle_ele){
                array[k] = arr[i];
                i++;
                k++;
            }
        }
        //for debugging
        System.out.println("The array (Merge sort) : " + Arrays.toString(array));
    }


    public void merge_sort(int[] arr,int lower_boundary,int upper_boundary){
        if (lower_boundary < upper_boundary){
            int middle_element = (lower_boundary + upper_boundary)/2;
            merge_sort(arr,lower_boundary,middle_element);
            merge_sort(arr,middle_element+1,upper_boundary);
            merge(arr,lower_boundary,middle_element,upper_boundary);
        }
    }
}
