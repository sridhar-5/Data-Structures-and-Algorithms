#include <iostream>

using namespace std;

void swap(int* m,int* n){
  int temp = *m;
  *m = *n;
  *n = temp;
}

void selection_sort(int array[],int n){

  int minimum_element;
  for(int i = 0 ; i < n;i++){
    minimum_element = i;
    for(int j = i + 1;j < n;j++){
      if(array[j] < array[minimum_element]){
        minimum_element = j;
      }
    }
    swap(&array[minimum_element],&array[i]);
  }

}
void printArray(int array[],int n){
  cout << "Array : ";
  for(int i = 0; i < n;i++){
    cout << array[i];
  }
}
int main(){
  int a[] = {6,2,9,4,1};
  int n = sizeof(a) / (sizeof(a[0]));
  selection_sort(a,n);
  printArray(a,n);
}
