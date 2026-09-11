a=6
b=0

while(True):
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("0.exit")

    n = int(input("Select yr choice"))
    match n:
        case 1:
            print(a+b)
        case 2:
            print(a-b)
        case 3:
            print(a*b)
        case 4:
            if(b==0):
                print("invalid no")
            else:
                print(1/b)
        case 0:
            exit(0)
        case _:
            print("wrong choice")
        