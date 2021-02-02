N,M=map(int, input().split())
nums=list(map(int, input().split()))
sums=[]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            ans = nums[i]+nums[j]+nums[k]
            if ans <= M:
                sums.append(ans)
print(max(sums))
