//area and perimeter of circle
import java.util.Scanner;
public class w1q6 {
    public static void main(String[] args) {
        Scanner i = new Scanner(System.in);
        System.out.println("Enter radius: ");
        double r=i.nextDouble();

        System.out.println("Area= " + 3.14*r*r);
        System.out.println("Perimeter=" + (2.0*3.14*r));
    }
}


