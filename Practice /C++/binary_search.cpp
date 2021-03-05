#include <iostream>

using namespace std;

int binary_search(int a[],int size,int ele){

  int middle_element;
  int l = 0;
  int r = size - 1;
  while(r >= l){
    middle_element = l + (r-l) / 2;

    if(a[middle_element] == ele){
      return middle_element;
    }

    else if(a[middle_element] < ele){
      l = middle_element + 1;
    }
    else{
      r = middle_element - 1;
    }
  }
}

int main(){

  int array[] = {1,3,4,5,6};
  int size_of_the_array = sizeof(array)/sizeof(array[0]);
  int element = 5;
  int found = binary_search(array,size_of_the_array,element);
  cout << found;
  return 0;
}
