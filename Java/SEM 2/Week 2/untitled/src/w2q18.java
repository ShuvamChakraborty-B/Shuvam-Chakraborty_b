//question 17
import java.util.Arrays;
import java.util.Scanner;
public class w2q18 {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the number of elements in the set: ");
            int n = scanner.nextInt();

            double[] numbers = new double[n];

            System.out.println("Enter the elements of the set:");
            for (int i = 0; i < n; i++) {
                numbers[i] = scanner.nextDouble();
            }

            double median = findMedian(numbers);

            System.out.println("Median of the set is: " + median);
        }

        static double findMedian(double[] numbers) {
            Arrays.sort(numbers);

            if (numbers.length % 2 == 0) {
                int middle1 = numbers.length / 2 - 1;
                int middle2 = numbers.length / 2;
                return (numbers[middle1] + numbers[middle2]) / 2.0;
            } else {
                int middle = numbers.length / 2;
                return numbers[middle];
            }
        }
    }

