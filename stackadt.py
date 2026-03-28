class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    
    def pop(self):
        if self.isEmpty():
            print("Underflow! Cannot pop from empty stack.")
            return None
        popped = self.stack.pop()
        print(f"Popped: {popped}")
        return popped

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top Element (Peek): {self.stack[-1]}")
        return self.stack[-1]

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Size of stack
    def size(self):
        return len(self.stack)

    # Display final stack state
    def display(self):
        print("Final Stack State:", self.stack)


# Meaningful Use: Parentheses Checking using Stack
def check_parentheses(expression):
    s = StackADT()
    for char in expression:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.isEmpty():
                return "Unbalanced Expression"
            s.pop()
    if s.isEmpty():
        return "Balanced Expression"
    else:
        return "Unbalanced Expression"


# Main Program (Input / Output Based)
if __name__ == "__main__":
    stack = StackADT()

    print("Enter number of operations:")
    n = int(input())

    print("Enter operations (push x / pop / peek):")
    for _ in range(n):
        operation = input().strip().split()

        if operation[0].lower() == "push":
            stack.push(operation[1])

        elif operation[0].lower() == "pop":
            stack.pop()

        elif operation[0].lower() == "peek":
            stack.peek()

        else:
            print("Invalid operation")

    # Show size and final stack
    print("Stack Size:", stack.size())
    stack.display()

    # Real Task: Expression Checking
    expr = input("Enter an expression to check parentheses: ")
    result = check_parentheses(expr)
    print("Parentheses Check:", result)
    