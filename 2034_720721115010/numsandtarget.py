def twoSum(nums,target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
nums = [3,2,4]
target = 6
print(twoSum(nums,target))