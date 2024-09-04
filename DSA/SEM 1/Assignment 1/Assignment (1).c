// 1. Write a C program to print an array.
#include <stdio.h>
int main()
{
    int size;
    printf("Enter max size of the array: ");
    scanf("%d", &size);
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        printf("Enter value for %d block: ", i);
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < size; i++)
    {
        printf(" value for %d block is : %d \n", i, arr[i]);
    }
    return 0;
}