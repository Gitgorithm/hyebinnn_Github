max=int(input())
datas=[0 for i in range(23)]
numbers=list(map(int,input().split()))
for i in range(max):
    for j in range(1,24):
        if numbers[i]==j: datas[j-1]=datas[j-1]+1
for i in range(23):
    print(datas[i])
