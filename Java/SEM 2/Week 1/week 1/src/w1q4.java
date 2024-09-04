import java.util.Scanner;
public class w1q4 {
    public static void main(String[] args) {
        Scanner r= new Scanner(System.in);
        System.out.println("Enter Fahrenheit= ");
        double c = r.nextDouble();
        double f = (c-32.0)*5.0/9.0;
        System.out.println("Celsius= " + f);


    }
}
