#half pyramid
# str=""
# for i in range(5):
#     str+="*"
#     print(str)


#inverted half pyramid
# for i in range(5,0,-1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()     

#diamond
# n=int(input("Enter the rows : "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range (2*i+1):
#         print("*",end="")
#     print()        
# #bottom traingle
# for i in range(n-1):
#     #printing spaces
#     for j in range(i+1):
#         print(" ",end="")
#     #printing stars
#     for j in range(2*(n-i-1)-1):
#         print ("*",end="")
#     print()


#hollow diamond
# num=int(input("Enter Number of Rows"))
# for i in range(1,num+1):
#     for j in range(num , i ,-1):
#         print(" ",end='')
#     for k in range(2*i-1):
#         if k==0 or k==2*i-2:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
# for i in range(0,num):
#     for j in range(i ):
#         print(" ",end='')
#     for k in range(2*(num-i)-1):
#         if k==0 or k==2*(num-i)-2:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()    

