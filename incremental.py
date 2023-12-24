import math

def dist ( x1,x2,y1,y2):
    dist_x1 = abs(x1-x2)
    dist_x2 = abs(y1-y2)

    distance = math.sqrt((dist_x1*dist_x1) + (dist_x2*dist_x2))
    return distance



print(f"{dist(4,3,6,2):0,.2f}")