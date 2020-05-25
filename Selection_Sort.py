arr=[5,4,6,7,1]

for i in range(len(arr)-1):
	for k in range(i, len(arr)):
		min = arr[i]
		index = i
		if (arr[k] < arr[i]): #means arr[k] is new min
			min = arr[k]
			index=k
	tmp=arr[i]
	arr[i] = arr[index]
	arr[index]=tmp
	print("iteration", i, arr)


