//mile to kilometres
import java.util.Scanner;
public class w1q11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter mile : ");
        double a= sc.nextDouble();
        double b= a*1.60934;
        System.out.printf(" %2f miles = %2f kilometres",a,b);

    }
}
