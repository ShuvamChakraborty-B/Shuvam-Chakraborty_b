// A C program to swap first and last digits of a number.
#include <stdio.h>
#include <math.h>
void main()
{
    int num, digitcount, divide, first, last, mid, swap;
    printf("Enter an integer:");
    scanf("%d", &num);
    digitcount = log10(num);
    divide = pow(10, digitcount);
    first = num / divide; // 12345/10000=1
    last = num % 10;      // 12345%10=5
    mid = num % divide;   // 12345%10000=2345 (/ returns quotient and % returns remainder)
    mid = mid / 10;       // 234
    swap = last * divide + mid * 10 + first;
    // 5*10000+2345
    printf("The swapped value is: %d", swap);
}