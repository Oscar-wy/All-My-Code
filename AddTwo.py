def Search(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - nums[i]
        if complement in seen:
            print(seen[complement], i)
        else:
            seen[num] = i
Search([3,2,3,5,8,4], 9)