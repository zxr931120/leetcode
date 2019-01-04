nums = [2, 11, 15, 7]
target = 9

nums.sort()
print(nums)
result = [0, 0]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(i, j)
        sum = nums[i] + nums[j]
        if sum == target:
            result = [i, j]

print(result)

#accepted