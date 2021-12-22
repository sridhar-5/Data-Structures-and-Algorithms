package com.dsa;

import java.util.Arrays;

public class BinarySearch {
    public static void main(String[] args){
        // test Linear Search for 1 D array
        int[] array = {2,3,5,6,7,89};
        System.out.println(BinarySearch1DArray(array, 89));

        int[] array2 = {98,92,91,89,35,34};
        System.out.println(AgnosticOrder(array2, 89));
//        int[][] array2 = {
//                {2,3,5,6,7,89,32},
//                {1,23,21,42,56,78,8},
//                {92,235,55,67,89,243,32}
//        };

//        System.out.println(Arrays.toString(LinearSearch2DArray(array2, 23)));
    }
    //iterative
    public static int BinarySearch1DArray(int[] arr,int target){
        int start = 0;
        int end = arr.length - 1;

        while(start <= end){
            int mid = start + (end - start) / 2;

            if(arr[mid] == target){
                return mid;
            }else if (arr[mid] > target){
                // target is in left subarray
                end = mid - 1;
            }else{
                //element is in right sub array
                start = mid + 1;
            }
        }
        return -1;
    }

    public static int AgnosticOrder(int[] arr, int target){

        boolean isAscending = arr[0] < arr[arr.length-1];
        int start = 0;
        int end = arr.length - 1;

        while(start <= end){
            int mid = start + (end - start)/2;

            //element is found
            if(arr[mid] == target){
                return mid;
            }
            else{
                if(isAscending){
                    if(arr[mid] > target){
                        end = mid - 1;
                    }else{
                        start = mid + 1;
                    }
                }else{
                    if(arr[mid] > target){
                        start = mid + 1;
                    }else{
                        end = mid - 1;
                    }
                }
            }
        }
        return -1;
    }
}
