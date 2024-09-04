// 1. Write a C program to read a 2D array (with most of the elements as 0s) and then represent
// the same array as Sparse Metrics.

#include <stdio.h>
int r, c;
void main()
{
    printf("Enter the number of rows and columns: ");
    scanf("%d %d", &r, &c);
    int a[r][c];
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("Enter the values for %d %d: ", i, j);
            scanf("%d", &a[i][j]);
        }
    }
    printf("Value Entered --- \n");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%d", a[i][j]);
        }
        printf("\n");
    }

        printf("Sparse Metrice representation: \n");
    int nonzeroelements = 0;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (a[i][j] != 0)
            {
                printf("row= %d column =%d value = %d \n", i, j, a[i][j]);
                nonzeroelements++;
            }
        }
    }
    printf("\n");
    printf("Non zero element count = %d", nonzeroelements);
}