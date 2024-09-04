// 11. Write a C program to check duplicate number in an array.

#include <stdio.h>
int main()
{
    int size, flag = 0;
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
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (a[i] == a[j])
            {
                flag = 1;
                break;
            }
        }
    }
    printf("\n");
    if (flag == 1)
    {
        printf("There is/are duplicates in the array");
    }
    else
    {
        printf("No duplicates found");
    }

    return 0;
}