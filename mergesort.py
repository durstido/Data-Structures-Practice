def mergesort(arr):
	if (len(arr)>1):
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		mergesort(left)
		mergesort(right)

		#indexes for each array
		left_i = 0
		right_i = 0
		arr_i = 0

		while right_i<len(right) and left_i<len(left): #while there is still elements in both lists
			if (right[right_i] < left[left_i]): #if curr elem in right < element in left, add right elem
				arr[arr_i] = right[right_i]
				right_i += 1
				arr_i += 1
			else: #else, add left elem
				arr[arr_i] = left[left_i]
				left_i += 1
				arr_i += 1

		#in case there are leftover elements in right array
		while right_i < len(right):
			arr[arr_i] = right[right_i]
			right_i += 1
			arr_i += 1

		#in case there are leftover elements in left array
		while left_i < len(left):
			arr[arr_i] = left[left_i]
			left_i += 1
			arr_i += 1

	return arr

arr = [54,26,93,17,77,31,44,55,20]
print(mergesort(arr))

