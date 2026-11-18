def get_max(*num):
    ma = len(num[0])

    for i in num:
        if len(i)>ma:
            ma = len(i)
            t = i
    return (ma,t)
# print(max(1,4,7,3,22,24))
print(get_max('sdfhs','fbhjgtds','sham','shravasti'))
