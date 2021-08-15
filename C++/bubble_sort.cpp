#include <iostream>

using namespace std;

void swap(int* m,int* n){
  int temp = *m;
  *m = *n;
  *n = temp;
}

void bubble_sort(int array[],int n){
  for(int i = 0;i < n;i++){
    for(int j = 0;j < n-i-1;j++){
      if(array[j] > array[j+1]){
        swap(&array[j],&array[j+1]);
      }
    }
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
  bubble_sort(a,n);
  printArray(a,n);
}
