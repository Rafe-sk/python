def main():
    a=10
    b=55
    #print("in function main....dir()=%s" % (dir()))
    print("in function main....dir()=",dir())
    result=absdiff(a,b)
    #print("the absolute value of %d - %d = %d" % (a,b,result))
    print("the absolute of ", a, "-", b, "=", result )

def absdiff(x,y):
    #print("in function main....dir()=%s" % (dir()))
    print("in function main....dir()=",dir())
    if x>y:
        z=x-y
    else:
        z=y-x
    return z

main()        