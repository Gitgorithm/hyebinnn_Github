h,w=map(int,input().split())
board = [[0]*w for i in range(h)]   # h열 w행 배열
n=int(input())
for i in range(n):
    l,d,x,y=map(int,input().split())
    if d==0:
        for j in range(l):
            board[x-1][y-1]=1
            y=y+1
    elif d==1:
        for j in range(l):
            board[x-1][y-1]=1
            x=x+1        
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()
