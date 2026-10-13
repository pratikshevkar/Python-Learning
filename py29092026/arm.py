n = 15
nn = n

lens = len(str(n))
sum = 0
while(n!=0):
    d = n%10
    sum = pow(d,lens) +sum
    n = n//10

if(sum==nn):
    print("arm")
else:
    print("not")