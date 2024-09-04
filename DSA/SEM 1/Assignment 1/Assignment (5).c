//Write a C program to print the largest and second largest element of the array.
#include<stdio.h>
int main(){
    int max=0,smax=0,length;
    printf("Enter the size of the integer array: ");
    scanf("%d",&length);
    int arr[length];
    for(int i=0;i<length;i++){
        printf("Enter integer value for %d block: ",i);
        scanf("%d",&arr[i]);

    }
    //again
     for(int i=0;i<length;i++){
        if(arr[i]>max){
            smax=max;
            max=arr[i];
        }
        else if (arr[i]>smax && arr[i]!=max)
        {
            smax=arr[i];
        }
        

    }
    printf("The largest integer is %d and second largest is %d",max,smax);
    return 0;
}