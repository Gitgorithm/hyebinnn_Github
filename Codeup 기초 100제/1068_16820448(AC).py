grade=int(input())
m=grade//10
if m==9 or m==10:
    print('A')
elif m==7 or m==8:
    print('B')
elif m>=4 and m<=6:
    print('C')
else: print('D')
