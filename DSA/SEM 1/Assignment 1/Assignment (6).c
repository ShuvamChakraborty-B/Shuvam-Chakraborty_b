// 6. Write a C program to display Fibonacci series.
#include <stdio.h>
void main()
{

    int a = 0, b = 1, c, d;
    printf("Enter the number of terms: ");
    scanf("%d", &d);
    for (int i = 1; i <= 5; i++)
    {
        printf(" %d ", a);
        c = a + b;
        a = b;
        b = c;
    }
}