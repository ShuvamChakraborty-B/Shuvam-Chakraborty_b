import java.util.Scanner;
public class w1q3 {
    public static void main(String[] args) {
        Scanner r= new Scanner(System.in);
        System.out.println("Enter Celsius: ");
        double c = r.nextDouble();
        double f = (9.0/5.0 *c + 32.0);
        System.out.println("Fahrenheit= " + f);


    }
}
