list = [1,3,6,3,6,32]

n = len(list)

for i in range(n):
    for j in range(i+1,n):
        if list[i]> list[j]:
            list[i] ,list[j] = list[j] ,list[i]

print(list)
