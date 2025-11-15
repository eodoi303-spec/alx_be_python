size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to control the rows
while row < size:
    # Use a for loop to print asterisks across the row
    for i in range(size):
        print("*", end="")
    # Move to the next row
    print()
    row += 1
