arr = [5,1,4,8,2]

for i in range(len(arr)-1):
	print(i)
	for k in range(len(arr)-i-1):
		if(arr[k] > arr[k+1]):
			tmp=arr[k]
			arr[k] = arr[k+1]
			arr[k+1] = tmp
		print(k, arr)


