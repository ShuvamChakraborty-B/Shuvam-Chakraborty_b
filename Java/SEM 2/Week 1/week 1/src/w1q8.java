//Write a Java Program to display whether a number is +ve or -ve
import java.util.Scanner;
public class w1q8 {
    public static void main(String[] args) {
        Scanner n= new Scanner(System.in);
        System.out.println("Enter an integer : ");
        int no=n.nextInt();
        if(no>0){
            System.out.println("Its positive");
        }
        else if(no==0){
            System.out.println("Its 0");
        }
        else{
            System.out.println("Its negative");
        }


    }
}
