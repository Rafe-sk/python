#WAP that takes a sentence as input and counts the no of words in it
a = input("Enter the sentence : ")

count = 1

for i in a:
    if(i == " "):
        count+= 1

print(count)