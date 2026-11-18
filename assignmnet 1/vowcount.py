#this program counts the vowels in givin string

seq = input("enter something")
count=0

for i in seq:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count =count+1
print(count)