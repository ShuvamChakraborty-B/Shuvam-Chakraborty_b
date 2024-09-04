//5. Write a program to display n number of elements. Memory should be allocated dynamically
//using calloc( ).
#include <stdio.h>
#include<stdlib.h>
#include <string.h>
int main()
{
    int a, *ptr;
    printf("Enter the size of the array: ");
    scanf("%d", &a);
    ptr = (int *)calloc(a , (sizeof(int)));
    for (int i = 0; i < a; i++)
    {
        printf("Enter the value for block %d : ", i);
        scanf("%d", &ptr[i]);
    }
    for (int i = 0; i < a; i++)
    {
        printf("The value for block %d :%d \n", i, ptr[i]);
    }
    return 0;
}