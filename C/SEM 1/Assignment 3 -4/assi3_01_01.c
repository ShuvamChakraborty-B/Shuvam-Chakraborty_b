//Write a C program to find maximum between two numbers.
#include<stdio.h>
void main(){
    int a,b,c;
    printf("Enter 1st integer: ");
    scanf("%d",&a);
    printf("Enter 2nd integer: ");
    scanf("%d",&b);
    if(a>b){
        printf("%d is greater",a);
    }
    else if(b>a){
        printf("%d is greater",b);}
    else{
        printf("Both are equal");
    }
}