public class w2q23 {


        public static void main(String[] args) {
            int currentNumber = 1;

            for (int i = 1; i <= 3; i++) {
                for (int j = 1; j <= i; j++) {
                    System.out.print(currentNumber + " ");
                    currentNumber++;
                }
                System.out.println();
            }
        }
    }


