# here we are removing duplicates from list using set

# li = [1,3,5,6,5]
# nli = set(li)

# l2 = list(nli)

# print(l2)

l1 = [1,3,5,3]
l2 = []

n=len(l1)

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)
