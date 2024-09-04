// Write a C program to count number of digits in a number.
#include <stdio.h>
#include <math.h>
void main()
{
    int num, count = 0, digit;
    printf("Enter the required number:");
    scanf("%d", &num);
    digit = num;
    do
    {
        digit = digit / 10;
        count++;
    } while (digit != 0);
    printf("No. of digits = %d", count);
    // return 0;
}