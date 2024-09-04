// 2. Write a C program to check whether a given string is Palindrome or not.
#include <stdio.h>
#include<string.h>
int main()
{
    char str1[1000];
    int i, flag = 0;
    printf("Enter the string to check for pallindrome: ");
    gets(str1);

    int length = strlen(str1);
    // strrev(str2);
    for (i = 0; i < length; i++)
    {
        if (str1[i] != str1[length - i - 1])
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
    {
        printf("It's a pallindrome!");
    }
    else
    {
        printf("It's not a pallindrome! ");
    }
    return 0;
}
