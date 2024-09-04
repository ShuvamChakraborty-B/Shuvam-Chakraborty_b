#include <stdio.h>
//bubble sort
void printArray(int *A,int a){
    for(int i=0;i<a;i++){
        printf("%d ",A[i]);
    }
    printf("\n");
}
//bubble sort
void BubbleSort(int *A, int a,int *count){
    int temp;
    int isSorted=1;
    for(int i=0;i<a-1;i++){
        printf("Working on iteration number : %d\n",i+1);
         *count=i+1;
        for(int j=0;j<a-1-i;j++){
            if(A[j]>A[j+1]){
                temp=A[j];
                A[j]=A[j+1];
                A[j+1]=temp;
                isSorted=0;
               
            }
            
           printArray(A,a);
        }
        if(isSorted){
            return;
        }
    }
}

// Function to swap two elements, quick sort
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to partition the array and return the pivot index ,quick sort
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// Function to perform the Quick Sort algorithm
void quickSort(int arr[], int low, int high,int *count) {
    //int count=0;
    if (low < high) {
        
        // Find the pivot index such that elements smaller than the pivot are on the left, and larger are on the right
        int pivotIndex = partition(arr, low, high);

        // Recursively sort the sub-arrays
        quickSort(arr, low, pivotIndex - 1,count);
        quickSort(arr, pivotIndex + 1, high,count);
        (*count)++;
        // Print the array after each iteration
        //for(int count =1 ; count<high; count++){
        
        printf("Iteration : " );
        for (int i = low; i <= high; i++) {
            
            
            printf("%d ", arr[i]);
            
        }
        printf("\n");
        //count++;
    }
   //printf("Total no of iterations: %d",count);
}
//}

int main() {
    int arr[] = {27, 15, 39, 21, 28, 70};
    int count=0;
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");
    printf("Performing Quick Sort--\n");
    // Call the Quick Sort function
    quickSort(arr, 0, n - 1,&count);
   
    
    printf("\nSorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");
    
    printf("Total no of iterations: %d \n",count);
    printf("\n\n");
     int A[]={27,15,39,21,28,70};
    int n1=6;
    printf("Performing Bubble Sort--\n");
    BubbleSort(A,n1,&count);
    //printArray(A,n);
    printf("Total no of iterations: %d \n",count);
    printf("As Quick Sort has less iterations than Bubble sort hence its better");

    return 0;
}






   
    
