flag = 0
num = 5
for i in range(2,(num//2)):
    if(num%i==0):
        flag = 1

if(flag == 0):
    print("prime")
else:
    print("not prime")