array=[[0 for col in range(19)] for row in range(19)]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    array[x-1][y-1]=1
for i in range(len(array)):  # 행 개수
    for j in range(len(array[i])):   # 1행, 2행 ... (요소)
        print(array[i][j], end=' ')
    print()   
