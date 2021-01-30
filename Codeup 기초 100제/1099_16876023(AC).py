array=[]
for i in range(10):
    gaemi=list(map(int,input().split()))
    array.append(gaemi)   #개미상자 현상황
x,y=1,1
while True:
    if array[x][y]==2:
            array[x][y]=9
            break      
    elif array[x][y+1]==1: 
        if array[x+1][y]==1:
            array[x][y]=9
            break
        else:  # 오른쪽은 1 아래는 0
            array[x][y]=9
            x=x+1
    else:   # 오른쪽 0 
        array[x][y]=9
        y=y+1  # 행의 오른쪽으로 이동 (y==열)
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()
