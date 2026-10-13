while True:
    print("1. +\n2. -\n3. *\n4. \\ \n5. !\n 6. press 0 for exit")
    n = input("Select your choice")
    match n:
        case '+':
            n1 = int(input("enter no 1 "))
            n2 = int(input("enter no 2 "))
            print(n1+n2)
        case '-':
              n1 = int(input("enter no 1 "))
              n2 = int(input("enter no 2 "))
              print(n1-n2)
        case '*':
                n1 = int(input("enter no 1 "))
                n2 = int(input("enter no 2 "))
                print(n1*n2)
        case '/':
                n1 = int(input("enter no 1 "))
                n2 = int(input("enter no 2 "))
                print(n1/n2)
        case '!':
                n1 = int(input("enter no "))
                fact = 1
                while(n1>0):
                      fact = fact * n1
                      n1 = n1-1
                print(fact)
        case '0':
                exit(0)
        case _:
                print("wrong choice entered")
