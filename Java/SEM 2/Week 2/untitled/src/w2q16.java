import java.util.Scanner;

public class w2q16 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("1. Convert Binary to Decimal");
        System.out.println("2. Convert Decimal to Binary");
        System.out.print("Choose an option (1 or 2): ");
        int option = scanner.nextInt();

        switch (option) {
            case 1:
                System.out.print("Enter a binary number: ");
                long binaryNum = scanner.nextLong();
                long decimalNumber = convertBinaryToDecimal(binaryNum);
                System.out.println("Decimal equivalent: " + decimalNumber);
                break;

            case 2:
                System.out.print("Enter a decimal number: ");
                long decimalNum = scanner.nextLong();
                String binaryEquivalent = convertDecimalToBinary(decimalNum);
                System.out.println("Binary equivalent: " + binaryEquivalent);
                break;

            default:
                System.out.println("Invalid option. Please choose 1 or 2.");
        }
    }

    static long convertBinaryToDecimal(long binaryNum) {
        long decimalNumber = 0;
        int i = 0;

        while (binaryNum != 0) {
            long remainder = binaryNum % 10;
            binaryNum /= 10;
            decimalNumber += remainder * Math.pow(2, i);
            ++i;
        }

        return decimalNumber;
    }

    static String convertDecimalToBinary(long decimalNum) {
        StringBuilder binaryEquivalent = new StringBuilder();

        while (decimalNum != 0) {
            long remainder = decimalNum % 2;
            binaryEquivalent.insert(0, remainder);
            decimalNum /= 2;
        }

        return binaryEquivalent.toString();
    }
}
