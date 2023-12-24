# wap that defines a list of countries that are a member of brics and check whether a country is a member of brics or not
BRICS=['BRAZIL','RUSSIA','INDIA','CHINA','SOUTH AFRICA']
ask=input("Enter the country name to check if it is in brics or not: ")
if ask.upper() in BRICS:
    print(ask,'is the part of BRICS')
else:
    print(ask,'is the not the part of BRICS')