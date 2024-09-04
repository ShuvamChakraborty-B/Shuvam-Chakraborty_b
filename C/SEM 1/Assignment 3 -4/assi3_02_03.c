//Write a C program to check whether a number is negative, positive or zero.
#include<stdio.h>
int main(){
    int a;
    printf("Enter the integer: ");
    scanf("%d",&a);
    if(a>0){
        printf("The number is positive");

    }
    else if(a<0){
        printf("The number is negative");

    }
    else if(a==0){
        printf("The number entered is 0");
    }
    return 0;

}