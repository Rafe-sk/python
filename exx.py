hrs3={"C":10,"B":20,"T":20,"S":5,"BC":5,"M":5}
hrs3Plus={"C":20,"B":30,"T":30,"S":10,"BC":10,"M":10}
vehicle={"C":"Car","B":"Bus","T":"Truck","S":"Scooter","BC":"Bycycle","M":"Motorbike"}
n=input("Enter Your Name ")
x=input("enter the type of vehicle (c for car, s/bc/m for 2 wheeler,t/ b for bus and truck) ").upper()
inTime=float(input("enter the time of entry (24 format(eg: 3.5 for 3:30))"))
outTime=float(input("enter the time of exit (24 format(eg: 3.5 for 3:30))"))
t=outTime-inTime
extratime=t-3
if t >3:
    fixedcharge=hrs3[x]*3
    
    charge=fixedcharge+hrs3Plus[x]*extratime
else:
    charge=hrs3[x]*t
print("____________Inparrking______________")
print("Name        :",n,"\n\nVehicle type:__|Hours____Rent______")

print(vehicle[x],"           |",t,"   ",charge)