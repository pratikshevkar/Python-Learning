while(True):
    bal = 85646
    print("1. check balance\n2.deposite\n3.withdraw\n4.exit")
    n = int(input("enter yr choice"))
    match (n):
        case 1:
            print(bal)
        case 2:
            print("deposite")
        case 3:
            if(bal>0):
                print("can withdraw")
            else:
                print("can't withdraw")
        case 4:
            exit(0)
        case _:
            print("wrong choice")
