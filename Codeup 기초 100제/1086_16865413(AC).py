w,h,b=map(int,input().split())
byte=w*h*b/8
print('%.2f MB' % (byte*2**-20))
