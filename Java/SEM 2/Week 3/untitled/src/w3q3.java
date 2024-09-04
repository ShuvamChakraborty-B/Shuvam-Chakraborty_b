import java.util.Scanner;

 class QueueUsingArray {

    private static final int MAX_SIZE = 100;
    private int[] queueArray;
    private int front, rear;

    public QueueUsingArray() {
        queueArray = new int[MAX_SIZE];
        front = -1;
        rear = -1;
    }

    public void enqueue(int value) {
        if (rear == MAX_SIZE - 1) {
            System.out.println("Queue Overflow. Cannot enqueue element: " + value);
            return;
        }

        if (front == -1) {
            front = 0;
        }

        queueArray[++rear] = value;
        System.out.println(value + " enqueued to the queue.");
    }

    public void dequeue() {
        if (front == -1) {
            System.out.println("Queue Underflow. Cannot dequeue from an empty queue.");
            return;
        }

        int dequeuedValue = queueArray[front++];
        System.out.println("Dequeued element: " + dequeuedValue);

        if (front > rear) {
            // Reset front and rear when the last element is dequeued
            front = -1;
            rear = -1;
        }
    }

    public void display() {
        if (front == -1) {
            System.out.println("Queue is empty.");
            return;
        }

        System.out.print("Queue elements: ");
        for (int i = front; i <= rear; i++) {
            System.out.print(queueArray[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        QueueUsingArray queue = new QueueUsingArray();
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nQueue Operations:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the element to enqueue: ");
                    int value = scanner.nextInt();
                    queue.enqueue(value);
                    break;
                case 2:
                    queue.dequeue();
                    break;
                case 3:
                    queue.display();
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
