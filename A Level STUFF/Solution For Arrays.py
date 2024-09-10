nums = []
total = 0
for i in range(6):
    nums.append(int(input("Enter A Number: ")))
    total += nums[i]
for i in range(5, -1, -1):
    print(nums[i])
print("Total Is", total)
print("Average Is", total/len(nums))