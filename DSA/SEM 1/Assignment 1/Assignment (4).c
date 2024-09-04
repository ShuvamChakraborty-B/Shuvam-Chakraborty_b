//_4. Write a C program to sort an array. //bubble sort
#include <stdio.h>
void printarr(int *a, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" %d ", a[i]);
    }
}

void sortarr(int *a, int n)
{
    for (int i = 0; i < (n - 1); i++)
    {
        for (int j = 0; j < (n - 1 - i); j++)
        {
            if (a[j] > a[j + 1])
            {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}
int main()
{
    int size;
    printf("Enter max size of the array: ");
    scanf("%d", &size);
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        printf("Enter integer value for %d block: ", i);
        scanf("%d", &arr[i]);
    }
    printarr(arr, size);
    printf("\n");
    sortarr(arr, size);
    printf("\n");
    printarr(arr, size);
    printf("\n");
    return 0;
}
