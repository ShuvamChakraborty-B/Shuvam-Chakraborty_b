import java.util.Scanner;
public class w2q20 {



        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read input values
            System.out.print("Enter the value of m: ");
            int m = scanner.nextInt();

            System.out.print("Enter the value of n: ");
            int n = scanner.nextInt();

            // Check if m is a multiple of n
            if (isMultiple(m, n)) {
                System.out.println(m + " is a multiple of " + n);
            } else {
                System.out.println(m + " is not a multiple of " + n);
            }
        }

        static boolean isMultiple(int m, int n) {
            // Check if m is a multiple of n
            return m % n == 0;
        }
    }

