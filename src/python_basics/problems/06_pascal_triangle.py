def pascal_triangle(n):
    for i in range(n):
        # Print leading spaces for alignment
        print(" " * (n - i), end="")

        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            # Calculate next value using formula
            num = num * (i - j) // (j + 1)
        print()  # Newline after each row


# Example usage
rows = int(input("Enter number of rows: "))
pascal_triangle(rows)
