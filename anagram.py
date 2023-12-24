#⁠wap to check if two strings are anagrams of each other.
str1=input("1st: ")
str2=input("2nd: ")
a=sorted(str1)
b=sorted(str2)
if a==b:
    print(str1,"&",str2,"are anagram")
else:
    print(str1,"&",str2,"are not anagram")