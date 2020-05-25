def ana(arr):
	
	if (arr==None):
		Return
	
	Dict = {}
	Output = []
	for word in arr:
		if (word==None):
			Break 
		sum=0
		for letter in word:
			print(letter)
			ascii = ord(letter)
			sum = sum + ascii
		if sum not in Dict:
			Dict[sum] = [word]
		else:
			tmp_arr = Dict[sum]
			tmp2_arr = tmp_arr.append(word)
			Dict[sum] = tmp_arr
			print("here", Dict[sum], sum)

	
	for element in Dict:
		Output.append(Dict[element]) 

	return Output

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(ana(arr))

