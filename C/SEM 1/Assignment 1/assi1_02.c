// prime no. from 1 to N
#include <stdio.h>
int isPrime(int a)
{
    for (int i = 2; i < a; i++)
    { // 2<2 is false, so it returns 1
        if (a % i == 0)
        {return 0; }
    }
    return 1;
}

void main()
{
    int a;
    printf("Enter the required range you want to print,from  1 to .. ");
    scanf("%d", &a);
    for (int b = 2; b <= a; b++)
    {
        if (isPrime(b))
        {
            printf("%d ", b);
        }
        // return 0;
    }
}