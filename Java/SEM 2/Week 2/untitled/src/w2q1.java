//1. Write a Java program to check whether a number is Buzz or not
import java.util.Scanner;
public class w2q1 {
    public static void main(String[] args){
        Scanner i = new Scanner(System.in);
        System.out.println("Enter an integer:");
        int a=i.nextInt();
        if(a%7==0 || a%10==7){
            System.out.println("Its a buzz number");
        }
        else{
            System.out.println("Its not a buzz number");
        }
    }
}