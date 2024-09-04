//Write a Java program to reverse a number.
import java.util.Scanner;
public class w2q4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the required integer: ");
        int b= sc.nextInt();
        int rev=0;
        while(b!=0){
            int digit=b%10;
            rev=rev*10+digit;
            b=b/10;

        }
        System.out.println(rev);
    }

}
