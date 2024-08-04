# 3. Write a Java program to implement Queue using array
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)


# Example usage
if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\n1. Enqueue")
        print("\n2. Dequeue")
        print("\n3. Front")
        print("\n4. Check if queue is empty")
        print("\n5. Size of queue")
        print("\n6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
            print(f"{item} added to the queue.")
        elif choice == 2:
            item = queue.dequeue()
            print(f"Dequeued item: {item}")
        elif choice == 3:
            item = queue.front()
            print(f"Front item: {item}")
        elif choice == 4:
            print("Queue is empty" if queue.is_empty() else "Queue is not empty")
        elif choice == 5:
            print(f"Size of queue: {queue.size()}")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
