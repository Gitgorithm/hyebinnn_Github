array=[]
for i in range(19):
    baduklist=list(map(int,input().split()))
    array.append(baduklist)   #바둑판 현상황
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    for j in range(19):
        if array[x-1][j]==0: array[x-1][j]=1
        else: array[x-1][j]=0
    for j in range(19):
        if array[j][y-1]==0: array[j][y-1]=1
        else: array[j][y-1]=0
        
for i in range(len(array)):  # 행 개수만큼 (행 하나씩) i==행
    for j in range(len(array[i])):   # 각 행 크기(길이)만큼 j==열
        print(array[i][j], end=' ')
    print()
        
