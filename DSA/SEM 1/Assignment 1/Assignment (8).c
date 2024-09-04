// Write a program that reads a 2D metrics and checks if the metrics is a symmetric metrics or not.
#include <stdio.h>
int main()
{
    int flag = 0, row, column;
    printf("Enter the number of row: ");
    scanf("%d", &row);
    printf("Enter the number of columns: ");
    scanf("%d", &column);

    int arr[row][column], trans[row][column];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {
            printf("Enter the value for %d %d: ", i, j);
            scanf("%d", &arr[i][j]);
        }
        printf("\n");
    }
    printf("The value of the matrix is: \n ");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {

            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {

            trans[j][i] = arr[i][j];
        }
    }
    printf("The transpose is: \n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {

            printf("%d ", trans[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {

            if (trans[i][j] != arr[i][j])
            {
                flag = 1;
                break;
            }
        }
    }
    if (flag == 1)
    {
        printf("It's not symmetric");
    }
    else
    {
        printf("It's symmetric");
    }

    return 0;
}