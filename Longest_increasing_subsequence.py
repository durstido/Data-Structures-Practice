
def longest_increasing_sub(nums):

	if(len(nums)==0):
		return 0

	table = [1 for i in range(len(nums))]
	Max = 1

	for i in range(1, len(nums)):
		for j in range(i):
			if (nums[j] < nums[i]):
				table[i] = max(table[j]+1, table[i])
		if table[i] > Max:
			Max = table[i]

	return Max

nums = [10,9,2,5,3,7,101,18]
print(longest_increasing_sub(nums))