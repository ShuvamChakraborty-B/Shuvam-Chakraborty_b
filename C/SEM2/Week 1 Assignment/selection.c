#include<stdio.h>
void printArray(int *A,int n){
    for(int i=0; i<n; i++){
        printf("%d ",A[i]);
    }
    printf("\n");
}

void selectionSort(int *A, int n){
    int indexofMin, temp;
    printf("Running Selection sort ...\n");
    for(int i=0; i<n-1;i++){
        indexofMin=i;
        printf("Iteration: %d \n",i+1);
        for(int j=i+1;j<n;j++){
            if(A[j]<A[indexofMin]){
                indexofMin=j;

            }
        }
        //Swap
        temp=A[i];
        A[i]=A[indexofMin];
        A[indexofMin]=temp;

        printArray(A,n);
    }
    
}

int main(){
    int A[]={27,15,39,21,28,70};
    int n=6;
    printArray(A,n);
    selectionSort(A,6);
    return 0;
}