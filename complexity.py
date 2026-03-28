# Aim: Develop intuition for time/space complexity using loop structures
# Input: n
# Output: Operation count + Big-O + 2-line justification

import math

# 1. Single Loop -> O(n)
def single_loop(n):
    count = 0
    for i in range(n):
        count += 1
    print("\n1. Single Loop")
    print("Estimated Operations:", count)
    print("Complexity: O(n)")
    print("Justification: Loop runs n times.")
    print("Operations increase linearly with input size.\n")


# 2. Nested Loop -> O(n^2)
def nested_loop(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print("2. Nested Loop")
    print("Estimated Operations:", count)
    print("Complexity: O(n^2)")
    print("Justification: Two loops each run n times.")
    print("Total operations ≈ n * n = n^2.\n")


# 3. Triangular Loop -> O(n^2)
def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            count += 1
    print("3. Triangular Loop")
    print("Estimated Operations:", count)
    print("Complexity: O(n^2)")
    print("Justification: Inner loop runs 1+2+...+n times.")
    print("Sum = n(n+1)/2 ≈ O(n^2).\n")


# 4. Halving Loop -> O(log n)
def halving_loop(n):
    count = 0
    i = n
    while i > 1:
        i = i // 2
        count += 1
    print("4. Halving Loop")
    print("Estimated Operations:", count)
    print("Complexity: O(log n)")
    print("Justification: Value is halved each iteration.")
    print("Number of steps ≈ log2(n).\n")


# Linear Search (Best, Average, Worst)
def linear_search_analysis():
    print("5. Linear Search Analysis")
    print("Best Case: O(1) – Element found at first position (e.g., search 5 in [5,2,3]).")
    print("Average Case: O(n) – Element found somewhere in the middle.")
    print("Worst Case: O(n) – Element at last position or not present (e.g., search 9 in [1,2,3,4]).\n")


# Binary Search (Best, Average, Worst)
def binary_search_analysis():
    print("6. Binary Search Analysis")
    print("Best Case: O(1) – Element found at middle in first comparison.")
    print("Average Case: O(log n) – Search space halves each step.")
    print("Worst Case: O(log n) – Element found after repeatedly dividing array (sorted array required).\n")


# Main Program (Input / Output)
if __name__ == "__main__":
    n = int(input("Enter value of n: "))

    single_loop(n)
    nested_loop(n)
    triangular_loop(n)
    halving_loop(n)

    linear_search_analysis()
    binary_search_analysis()