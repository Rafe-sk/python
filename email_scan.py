# wap that scans an email adress  and forms a tuple of user name and domain
# email=input("Enter the email address:- ")
# print(email)
# b=(email.split("@"))
# c=b[0]
# d=b[1]
# print("Username:-",c)
# print("Domain:-",d)

usernames=[]
domains=[]


for i in range(5):
      email=input('Enter the email adress:-')

      print(email)
      if '@' in email:
       username,domain=email.split('@')
       usernames.append(username)
       domains.append(domain)
       email_mytuple=(username,domain)
       print('User name:-',username)
       print('Domain:-',domain)
print(usernames)
print(domains)