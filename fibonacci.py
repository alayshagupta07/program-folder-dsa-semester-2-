# Aim: Understand inefficiency of naive recursion and benefit of memoization

# Global counters
naive_calls = 0
memo_calls = 0

# Naive Recursive Fibonacci
def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)



def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


# Function to compare both methods
def compare_fibonacci(n):
    global naive_calls, memo_calls

    # Reset counters and memo dictionary
    naive_calls = 0
    memo_calls = 0
    memo = {}

    # Calculate Fibonacci using naive recursion
    fib_n_naive = fib_naive(n)

    # Calculate Fibonacci using memoization
    fib_n_memo = fib_memo(n, memo)

    # Output Results
    print(f"\nFor n = {n}")
    print("Fibonacci Value:", fib_n_naive)
    print("Naive Recursive Calls:", naive_calls)
    print("Memoized Recursive Calls:", memo_calls)

    # Short Explanation (3–4 lines as required)
    print("Explanation:")
    print("Naive recursion recomputes the same subproblems many times.")
    print("For example, fib(5) is calculated repeatedly inside fib(6), fib(7), etc.")
    print("Memoization stores previously computed values to avoid repetition.")
    print("Hence, memoized version drastically reduces the number of function calls.\n")


# Main Program (Input / Output expectation)
if __name__ == "__main__":
    print("Enter n values separated by space (e.g., 10 20 30):")
    inputs = list(map(int, input().split()))

    for n in inputs:
        if n < 0:
            print(f"\nInvalid input for n = {n}. Fibonacci is defined for n ≥ 0.")
        else:
            compare_fibonacci(n)