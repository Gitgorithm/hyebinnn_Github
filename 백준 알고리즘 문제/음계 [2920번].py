nums=list(map(int, input().split()))
sortlist = sorted(nums)
xsortlist = list(reversed(sortlist))

if sortlist == nums:
    print('ascending')
elif nums == xsortlist:
    print('descending')
else:
    print('mixed')
