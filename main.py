nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

x = [num for idx, num in enumerate(nums) if num not in nums[:idx]]
print(x)