//3. Write a C program to convert temperature from degree Centigrade to Fahrenheit.
#include<stdio.h>
int main(){
    float cel, faren;
    printf("Enter the temperature in celsius: ");
    scanf("%f",&cel);
    faren=(cel*(9.0/5.0))+32.0;
    printf("The temperature in farenheit is : %f",faren);
    return 0;
}