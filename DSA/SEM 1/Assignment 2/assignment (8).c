// 8. Write a C program to search an element in an Array using dynamic memory allocation.
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int i1, j, *ptr, k = 0, b;
    printf("Enter the size of the array: ");
    scanf("%d", &i1);
    ptr = (int *)malloc(i1 * sizeof(int));
    for (int i = 0; i < i1; i++)
    {
        printf("Enter value for block %d: ", i);
        scanf("%d", &ptr[i]);
    }
    printf("Enter the element you want to find: ");
    scanf("%d", &j);
    for (int i = 0; i < i1; i++)
    {
        if (ptr[i] == j)
        {
            k = 1;
            b = i;
            break;
        }
    }
    if (k == 0)
    {
        printf("Element not found!");
    }
    else
    {
        printf("Element found! \n");
        printf("Its on block %d", b);
    }
    free(ptr);
    return 0;
}
