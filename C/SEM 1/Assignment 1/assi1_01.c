// factorial of a number
#include <stdio.h>
// int fact(int b);
int main()
{
    // int a,b;
    long long a, b, fact = 1;
    printf("Enter a positive integer:");
    scanf("%lld", &a);

    for (b = 1; b <= a; b++)
    {
        fact = fact * b;
    }
    printf("The factorial of the above integer %lld is %lld", a, fact);
    return 0;
}
