//area and perimeter of rectangle
import java.util.Scanner;
public class w1q5 {
    public static void main(String[] args) {
        Scanner i = new Scanner(System.in);
        System.out.println("Enter length: ");
        double l=i.nextDouble();
        System.out.println("Enter breadth");
        double b=i.nextDouble();
        System.out.println("Area= " + l*b);
        System.out.println("Perimeter=" + (2.0*(l+b)));
    }
}
