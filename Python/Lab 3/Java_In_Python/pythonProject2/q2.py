# 2. Write a Java program to implement stack using array.
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Example usage
if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n1. Push")
        print("\n2. Pop")
        print("\n3. Peek")
        print("\n4. Check if stack is empty")
        print("\n5. Size of stack")
        print("\n6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to push: ")
            stack.push(item)
            print(f"{item} pushed to stack.")
        elif choice == 2:
            item = stack.pop()
            print(f"Popped item: {item}")
        elif choice == 3:
            item = stack.peek()
            print(f"Top item: {item}")
        elif choice == 4:
            print("Stack is empty" if stack.is_empty() else "Stack is not empty")
        elif choice == 5:
            print(f"Size of stack: {stack.size()}")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
