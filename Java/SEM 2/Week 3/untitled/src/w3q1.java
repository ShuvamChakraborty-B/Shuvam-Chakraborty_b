import java.util.Scanner;
public class w3q1 {
    public static void main(String[] args) {


                Scanner scanner = new Scanner(System.in);

                // Read the size of the array
                System.out.print("Enter the size of the array: ");
                int size = scanner.nextInt();

                // Create an array
                int[] numbers = new int[size];

                // Read elements of the array
                System.out.println("Enter the elements of the array:");
                for (int i = 0; i < size; i++) {
                    numbers[i] = scanner.nextInt();
                }

                // Calculate sum and average
                int sum = calculateSum(numbers);
                double average = calculateAverage(numbers);

                // Display results
                System.out.println("Sum of the array elements: " + sum);
                System.out.println("Average of the array elements: " + average);
            }

            static int calculateSum(int[] array) {
                int sum = 0;
                for (int num : array) {
                    sum += num;
                }
                return sum;
            }

            static double calculateAverage(int[] array) {
                if (array.length == 0) {
                    return 0.0; // Avoid division by zero
                }
                return (double) calculateSum(array) / array.length;
            }
        }


