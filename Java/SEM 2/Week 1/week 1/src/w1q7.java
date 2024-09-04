//Write a Java Program to display whether a number is odd or even.
import java.util.Scanner;
public class w1q7 {
    public static void main(String[] args) {
        Scanner n= new Scanner(System.in);
        System.out.println("Enter an integer : ");
        int no=n.nextInt();
        if(no%2==0){
            System.out.println("Its even");
        }
        else{
            System.out.println("Its odd");
        }


    }
}
