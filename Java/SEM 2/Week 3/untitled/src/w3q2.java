import java.util.Scanner;

 class StackUsingArray {

    private static final int MAX_SIZE = 100;
    private int[] stackArray;
    private int top;

    public StackUsingArray() {
        stackArray = new int[MAX_SIZE];
        top = -1;
    }

    public void push(int value) {
        if (top == MAX_SIZE - 1) {
            System.out.println("Stack Overflow. Cannot push element: " + value);
            return;
        }
        stackArray[++top] = value;
        System.out.println(value + " pushed to the stack.");
    }

    public void pop() {
        if (top == -1) {
            System.out.println("Stack Underflow. Cannot pop from an empty stack.");
            return;
        }
        int poppedValue = stackArray[top--];
        System.out.println("Popped element: " + poppedValue);
    }

    public void display() {
        if (top == -1) {
            System.out.println("Stack is empty.");
            return;
        }
        System.out.print("Stack elements: ");
        for (int i = 0; i <= top; i++) {
            System.out.print(stackArray[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        StackUsingArray stack = new StackUsingArray();
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nStack Operations:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the element to push: ");
                    int value = scanner.nextInt();
                    stack.push(value);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    stack.display();
                    break;
                case 4:
                    System.out.println("Exiting the program.");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }

        } while (choice != 4);
    }
}
