year,month,day=map(int, input().split('.'))
print('%04d' % year, '%02d' % month, '%02d' % day, sep='.')
