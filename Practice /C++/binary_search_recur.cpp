#include <iostream>

using namespace std;

int binary_search(int a[],int l,int r,int element){
  if (r >= l){
    int middle_element = l + (r- l)/2;

    if(a[middle_element] < element){
      return binary_search(a,middle_element+1,r,element);
    }
    if(a[middle_element] > element){
      return binary_search(a,l,middle_element-1,element);
    }
    if(a[middle_element] == element){
      return middle_element;
    }
  }
}

int main(){

  int array[] = {1,3,4,5,6};
  int size_of_the_array = sizeof(array)/sizeof(array[0]);
  int element = 5;
  int found = binary_search(array,0,size_of_the_array-1,element);
  cout << found;
  return 0;
}
