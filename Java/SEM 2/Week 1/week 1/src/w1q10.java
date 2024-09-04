//swap
import java.util.Scanner;
public class w1q10 {
    public static void main(String[] args) {
        int a,b,c;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first integer :");
        a= sc.nextInt();
        System.out.println("Enter second integer :");
        b= sc.nextInt();
        c=a;
        a=b;
        b=c;
        System.out.printf("Values after swapping: %d  %d",a,b);

    }
}
