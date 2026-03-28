# Aim: Learn recursion basics: base case, recursive case, and stack growth

def factorial(n, depth=0):
    # Print indentation to visualize stack growth
    print("  " * depth + f"Call: factorial({n})")

    # Base Case
    if n == 0:
        print("  " * depth + "Base Case Reached: factorial(0) = 1")
        return 1

    # Recursive Case
    result = n * factorial(n - 1, depth + 1)

    # Print return value while stack unwinds
    print("  " * depth + f"Return: factorial({n}) = {result}")
    return result


# Main Program (Input / Output)
try:
    n = int(input("Enter a non-negative integer (n ≥ 0): "))

    # Reject invalid input
    if n < 0:
        print("Invalid Input! Factorial is only defined for n ≥ 0.")
    else:
        print("\n--- Call Stack Trace (for notebook) ---")
        answer = factorial(n)

        print("\nFinal Output:")
        print(f"Factorial({n}) = {answer}")

        # Complexity Statement (Required in Lab)
        print("\nComplexity Statement:")
        print("Time Complexity: O(n) - The function makes n recursive calls.")
        print("Space Complexity: O(n) - n calls are stored in the recursion call stack.")

except ValueError:
    print("Invalid Input! Please enter an integer.")