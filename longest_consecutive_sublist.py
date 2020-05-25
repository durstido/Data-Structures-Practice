
def longest_old(arr):

	Dict = {}

	Max = 0
	Max_list = []

	for element in arr:
		#if not seen it before 
		if element not in Dict:
			#if neither +1 or -1 are in it, create its own list
			if not (element+1 in Dict or element-1 in Dict):
				Dict[element] = [element]
				if (len(Dict[element]) > Max):
					Max = len(Dict[element])
					Max_list = Dict[element]

			else:
				#only +1 or only -1
				if(element+1 in Dict):
					tmp = Dict[element+1]
					tmp.append(element)
					Dict[element] = tmp

					if (len(Dict[element+1]) > Max):
						Max = len(Dict[element+1])
						Max_list = Dict[element+1]

				elif(element-1 in Dict):
					tmp = Dict[element-1]
					tmp.append(element)
					Dict[element] = tmp

					if (len(Dict[element-1]) > Max):
						Max = len(Dict[element-1])
						Max_list = Dict[element-1]

				#both
				elif(element-1 in Dict and element+1 in Dict):
					tmp_minus = Dict[element-1]
					tmp_plus = Dict[elemtn+1]
					tmp_minus.append(element)
					tmp_minus.append(tmp_plus)
					tmp_plus = tmp_minus

					if (len(Dict[element-1]) > Max):
						Max = len(Dict[element-1])
						Max_list = Dict[element-1]

	return Max, Max_list


def longest_ordered_arr(arr):

	if(len(arr)==0):
		return None

	max_curr=1
	max_all=1
	for i in range(1, len(arr)):
		if (arr[i-1] + 1 == arr[i]): #consecutive elements
			max_curr = max_curr + 1
		else: #start a new count
			max_curr = 1
		if (max_curr > max_all):
			max_all = max_curr

	return max_all


arr = [0, 5, 6, 1, 8, 2, 3]
#arr = [1,2,5,6,7,8,3,4,9,10,11,12]
print(longest_old(arr))





