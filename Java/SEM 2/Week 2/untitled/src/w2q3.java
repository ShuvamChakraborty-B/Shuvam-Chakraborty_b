//3. Write a Java program for Fibonacci series.
import java.util.Scanner;
public class w2q3 {
    public static void main(String[] args) {
        Scanner b= new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int a=b.nextInt();
        int firstitem=0, seconditem=1;
        for(int i=0;i<a;i++){
            System.out.print(firstitem + " ");
            int sum= firstitem+seconditem;
            firstitem=seconditem;
            seconditem=sum;
        }
    }


}
