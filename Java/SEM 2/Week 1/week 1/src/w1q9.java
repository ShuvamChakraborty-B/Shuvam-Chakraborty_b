//Write a Java program to find maximum of three numbers.
import java.util.Scanner;
public class w1q9 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter first number: ");
        int a= sc.nextInt();
        System.out.println("Enter second number: ");
        int b= sc.nextInt();
        System.out.println("Enter third number: ");
        int c= sc.nextInt();
        int max=a;
        if(max<b){
            max =b;
        }
        if (max<c) {
            max=c;
        }
        System.out.println("Maximum number: " + max);

    }
}
