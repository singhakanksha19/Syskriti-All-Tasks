# PY200_T5 — Chessboard with numbers
# Author  : Akanksha Singh

# Input from user
N = int(input("Enter value of N: "))

# Loop through rows
for row in range(N):
    # Loop through columns
    for col in range(N):
        # Diagonal condition first (highest priority)
        if row == col:
            print("X", end=" ")
        # Even condition
        elif (row + col) % 2 == 0:
            print("1", end=" ")
        # Else condition
        else:
            print("0", end=" ")
    print()  # Move to next line after each row