num=input()
for i in range(len(num)):
    print('['+str(int(num[i])*(10**(len(num)-(i+1))))+']')
