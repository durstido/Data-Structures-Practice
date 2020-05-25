from sys import stdin
from collections import OrderedDict

def main():
	lines = stdin.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].replace('\n', '')

	T = int(lines[0]) #number of tests
	j=2 #the element in which tests  start; 
	    #first element only says how many inputs are in this test

	for i in range(T): #for the number of tests
		pairs = []
		print("Case #{}:".format(i+1))

		for k in range(j+1, int(lines[j]) + j + 1): #from where curr test inputs starts until the end
													#lines[j] says how many inputs for this test
			pairs.append(lines[k].split(' ')) #read the fruit and value one by one
		solution(pairs)

		#print spaces between tests, excluding last test
		if (i!=T-1):
			print('')

		#go to next test
		j = int(lines[j]) + j + 2 

def solution(pairs):
	dict = {}

	for fruit, value in pairs:
		value = int(value)
		if fruit not in dict: #if not in dict, create a new entery for it
			new_dict = {'name':fruit, 'max':value, 'low':value, 'number':1, 'total':value, 'avg':value}
			dict[fruit] = new_dict

		else: #else; can't use if fruit in dict cuz we just created it, so of course it'd be in dict 
			curr_dict = dict[fruit]
			if value > curr_dict['max']:
				curr_dict['max'] = value
			if value < curr_dict['low']:
				curr_dict['low'] = value
			curr_dict['number'] = curr_dict['number'] + 1
			curr_dict['total'] = curr_dict['total'] + value
			curr_dict['avg'] = int(curr_dict['total'] / curr_dict['number'])

		#after we're done looping through current test's input and storing it correctly
	dict = OrderedDict(sorted(dict.items())) #sort the dict so it's alphabetical 
	for element in dict.keys():
		curr_dict = dict[element]
		print(curr_dict['name'], curr_dict['low'], curr_dict['max'], curr_dict['avg'])

if __name__ == "__main__":
    main()

