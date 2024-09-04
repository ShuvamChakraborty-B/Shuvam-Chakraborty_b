// 10. Write a C program to check the sum of all elements of an array

#include <stdio.h>
int main()
{
    int size, sum = 0;
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
    printf("The sum of elements is: ");
    for (int i = 0; i < size; i++)
    {
        sum=sum+a[i];
    }
    printf("%d",sum);
    return 0;
}