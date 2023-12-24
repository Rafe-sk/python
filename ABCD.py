rows = int(input("Enter the number"))
for i in range(rows):
    # Print leading spaces
    for j in range(i):
        print("", end=" ")
        

    # Print characters
    for k in range(i-2, rows):
        print(chr(65 + k+2), end=" ")
        

    # Move to the next line
    print()  