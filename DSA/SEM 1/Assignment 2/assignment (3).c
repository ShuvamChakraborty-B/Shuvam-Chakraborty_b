/*3. Write a C program to pass an array to a function using Call by Reference, update the array
values in the function, print the array elements both in the function and in the calling
function.*/

#include <stdio.h>
int main()
{
    int size;
    printf("Enter the size of an array: ");
    scanf("%d", &size);
    int a[size];
    for (int i = 0; i < size; i++)
    {
        printf("Enter the value for block %d: ", i);
        scanf("%d", &a[i]);
    }

    for (int i = 0; i < size; i++)
    {
        printf(" The value for block %d before function call: %d\n", i, a[i]);
    }
    funct(a, size);
    for (int i = 0; i < size; i++)
    {
        printf(" The value for block %d after function call: %d \n", i, a[i]);
    }
    return 0;
}
void funct(int *a, int size)
{
    for (int i = 0; i < size; i++)
    {
        a[i] = a[i] + 10;
        printf("Updated value of block %d inside function: %d \n", i, a[i]);
    }
}