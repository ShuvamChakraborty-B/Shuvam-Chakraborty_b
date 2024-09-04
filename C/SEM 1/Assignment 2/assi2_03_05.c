// Write a C program to check whether a number is Palindrome or not.
#include <stdio.h>
void main()
{
    int inp, originalnumber, dio, reverse = 0;
    printf("Enter your number ");
    scanf("%d", &inp);

    // pallindrome process starts here
    originalnumber = inp;
    while (inp != 0)
    {
        dio = inp % 10;
        reverse = reverse * 10 + dio;
        inp = inp / 10;
    }
    if (originalnumber == reverse){
        printf("It's a pallindrome");}
    else
    {
        printf("It's not a pallindrome");
    }
}