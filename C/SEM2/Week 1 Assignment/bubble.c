#include<stdio.h>
void printArray(int *A,int a){
    for(int i=0;i<a;i++){
        printf("%d ",A[i]);
    }
    printf("\n");
}
void BubbleSort(int *A, int a){
    int temp;
    int isSorted=1;
    for(int i=0;i<a-1;i++){
        printf("Working on iteration number : %d\n",i+1);
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
int main(){
    int A[]={27,15,39,21,28,70};
    int n=6;
    BubbleSort(A,n);
    //printArray(A,n);
    return 0;
}