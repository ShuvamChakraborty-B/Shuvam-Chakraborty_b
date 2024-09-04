// Write a C program to check whether a number is Armstrong number or not.

// Write a C program to check whether a number is Armstrong number or not.

#include <stdio.h>
#include <math.h>
void main()
{
    int i, count = 0, temp, remainder, result = 0, quotient;
    printf("Enter the required number: ");
    scanf("%d", &i);
    temp = i;
    // code to calculate the total no of digits
    do{ // code to calculate the total no of digits
        temp = temp / 10;  // quotient
        count++;
    } while (temp != 0);
    // printf("%d",count);
    // return 0;

    // calculate the armstrong number
    temp = i;
    while (temp != 0)
    {
        remainder = temp % 10; // remainder
        result = result + pow(remainder, count);
        temp = temp / 10;
    }
    // checking
    if (result == i)
    {
        printf("It's an armstrong number.");
    }
    else
        printf("It's not an armstrong number.");
}