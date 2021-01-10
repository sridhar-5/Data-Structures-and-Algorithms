#include <cmath>
#include <iostream>

using namespace std;

int linear_search(int element,int size_of_the_array,int arr[]){
  int i;

  /*time complexity for this search is O(n) in the worst case when the element is at the end of the array and
  the best case is o(1) when the element is in the first index of the array.*/
  for(i = 0;i < size_of_the_array;i++){
    if(arr[i] == element){
      return i;
    }
  }
  return -1;
}
int main(){
  int a[] = {1,2,3,4,5};
  int found = linear_search(5,5,a);
  cout << found;
}
