# Tower of Hanoi using Recursion (Lab Ready Code)

move_count = 0  # Global counter to count total moves


def hanoi(n, src, aux, dst, print_moves=True):
    global move_count
    
    if n == 1:
        move_count += 1
        if print_moves:
            print(f"Move disk 1 from {src} to {dst}")
        return
    
    # Move n-1 disks from source to auxiliary
    hanoi(n - 1, src, dst, aux, print_moves)
    
    # Move nth disk from source to destination
    move_count += 1
    if print_moves:
        print(f"Move disk {n} from {src} to {dst}")
    
    # Move n-1 disks from auxiliary to destination
    hanoi(n - 1, aux, src, dst, print_moves)


# ===== MAIN PROGRAM =====
n = int(input("Enter number of disks (n): "))

# 1. Print exact move sequence for n = 3 (Lab Requirement)
print("\nMove sequence for n = 3:")
move_count = 0
hanoi(3, 'A', 'B', 'C', True)

# 2. Show move count for n = 4 (Lab Requirement)
move_count = 0
hanoi(4, 'A', 'B', 'C', False)  # False = do not print moves
print("\nTotal number of moves for n = 4:", move_count)

# 3. Complexity Statement (Lab Requirement)
print("\nComplexity Statement:")
print("The number of moves follows recurrence: T(n) = 2T(n-1) + 1")
print("Hence, time complexity = O(2^n) (Exponential Growth)")