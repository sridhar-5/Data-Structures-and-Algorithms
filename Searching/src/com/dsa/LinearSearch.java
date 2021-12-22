package com.dsa;

import java.util.Arrays;

public class LinearSearch {
    public static void main(String[] args){
        // test Linear Search for 1 D array
        int[] array = {2,3,5,6,7,89,32};
        System.out.println(LinearSearch1DArray(array, 89));

        // test Linear Search for 2D array
        int[][] array2 = {
                {2,3,5,6,7,89,32},
                {1,23,21,42,56,78,8},
                {92,235,55,67,89,243,32}
        };

        System.out.println(Arrays.toString(LinearSearch2DArray(array2, 23)));
    }

    public static int LinearSearch1DArray(int[] arr, int target){
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == target){
                // element is found
                return i;
            }
        }
        // if element is not found
        return -1;
    }

    public static int[] LinearSearch2DArray(int[][] arr, int target){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if(arr[i][j] == target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{-1,-1};
    }
}
