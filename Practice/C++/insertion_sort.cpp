#include <iostream>
#include <cstdio>

using namespace std;

void print(int array[],int n){
  for(int i = 0; i < n;i++){
    cout << array[i];
    cout << " ";
  }
}
/*
   this algorithm works as such like first we consider the second element
   of the array as the key and search its predecesor element if it is greater
   then we keep searching for all the elemnts behind it till it reaches its
   correct position and then insert the element. while inserting we move all
   elemnts to the right by one step
*/
void insertion_sort(int array[],int size){
  int i,j,value;

  for(i = 1; i < size;i++){
    value = array[i];
    j = i - 1;

    /*
    this loop moves the elements after the key one step towards right and makes the
    value search for the element behind it and so on.
    */
    while( j >= 0 && array[j] > value){
      array[j+1] = array[j];
      j = j - 1;
    }
    array[j+1] = value;
  }
  print(array,size);
}
int main(){
  int array[] = {12,11,13,5,6};
  int n = sizeof(array)/sizeof(array[0]);

  //function call here
  insertion_sort(array,n);
}
