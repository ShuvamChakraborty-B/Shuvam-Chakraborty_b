import java.util.Scanner;

public class w2q9 {



        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the number for which you want to generate the multiplication table: ");
            int number = scanner.nextInt();

            System.out.print("Enter the range (number of terms) for the multiplication table: ");
            int range = scanner.nextInt();

            generateMultiplicationTable(number, range);
        }

        static void generateMultiplicationTable(int number, int range) {
            System.out.println("Multiplication table for " + number + " up to " + range + " terms:");

            for (int i = 1; i <= range; i++) {
                int result = number * i;
                System.out.println(number + " * " + i + " = " + result);
            }
        }
    }


