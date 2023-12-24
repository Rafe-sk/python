def distance(x1,x2,y1,y2):
    dist=(((x2-x1)**2)+((y2-y1)**2))
    return dist

distance(2,4,5,6)

def area():
    r=distance(2,4,5,6)
    area=r*r*3.14
    print("area",area)

area()