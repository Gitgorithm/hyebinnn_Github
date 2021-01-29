h,b,c,s=map(int,input().split())
byte = (h*b*c*s)/8
result = byte / (1024**2)
print('%.1f MB' % result)
