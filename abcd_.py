
for i in range(2):
    for j in range(2,i,-1):
        print("",end=" ")
    for k in range(i):
        print(chr(67-k+2),end=" ")

# for i in range(3):
#     # Print leading spaces
#     for j in range(i):
#         print("", end=" ")
        

#     # Print characters
#     for k in range(i-2, 3):
#         print(chr(65 + k+2), end=" ")
        

#     # Move to the next line
#     print()  