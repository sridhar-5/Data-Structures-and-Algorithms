
#include <iostream>
using namespace std;

 void merge(int A[ ] , int start, int mid, int end) {
 //stores the starting position of both parts in temporary variables.
int p = start ,q = mid+1;

int Arr[end-start+1] , k=0;

for(int i = start ;i <= end ;i++) {
    if(p > mid){      //checks if first part comes to an end or not .
       Arr[ k ] = A[ q] ;
       k++;
       q++;
    }
   else if ( q > end) {  //checks if second part comes to an end or not
       Arr[ k ] = A[ p ];
       k++;
       p++;
    }
   else if( A[ p ] < A[ q ]){     //checks which part has smaller element.
      Arr[ k ] = A[ p ];
      k++;
      p++;
   }
   else{
      Arr[ k ] = A[ q];
      k++;
      q++;
 }
}
  for (int p=0 ; p< k ;p ++) {
   /* Now the real array has elements in sorted manner including both
        parts.*/
     A[ start++ ] = Arr[ p ] ;
  }
}


void merge_sort (int A[ ] , int start , int end ){
    if( start < end ) {
    int mid = (start + end ) / 2 ;
    merge_sort (A, start , mid ) ;
    merge_sort (A,mid+1 , end ) ;
	merge(A,start , mid , end );

   }
}

int main(){
	int array[] = {6,9,4,1,8};
	int n = 5;
	merge_sort(array,0,n-1);
	for(int i = 0;i <n ;i++){
		cout << array[i] <<" ";
	}
}
