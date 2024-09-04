// Write a C program to print reverse array
#include <stdio.h>
int main()
{
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    int a[size];
    for (int i = 0; i < size; i++)
    {
        printf("Enter value for block %d : ", i);
        scanf("%d", &a[i]);
    }
    printf("The value you entered is : ");
    for (int i = 0; i < size; i++)
    {
        printf(" %d ", a[i]);
    }
    printf("The value in reverse are as follows: ");
    for (int i = size - 1; i >= 0; i--)
    {

        printf(" %d ", a[i]);
    }
    return 0;
}