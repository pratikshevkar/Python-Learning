l = [2,4,5,6,7]
min = l[0]
max = l[0]
for n in l:
    if(n<min):
        s = min
        min = n

    if(n>max):
        p = max
        max = n

print(min)
print(max)
print(p)
print(s)

