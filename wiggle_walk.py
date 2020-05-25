from sys import stdin
from collections import OrderedDict

def wiggle(T, N, R, C, Sr, Sc, Is):
	for i in range(T): #how many test cases we have

		curr = [Sr, Sc]
		visited = []
		visited.append(curr.copy()) 
			#can't add a list to a hashmap/hashset, has to be in values
			#use a hashset instead #set.add() not append()
			#to keep track of lists, add lists into a list of lists, but use list.copy()

		for i in range(N):
			if (Is[i] == 'N'): #increase row
				curr[0] = curr[0] - 1
			elif (Is[i] == 'S'): #decrease row
				curr[0] = curr[0] + 1
			elif (Is[i] == 'E'): #increase col
				curr[1] = curr[1] + 1
			elif (Is[i] == 'W'): #decrease col
				curr[1] = curr[1] - 1

			if curr not in visited:
				visited.append(curr.copy())
			else:
				while curr in visited:
					if (Is[i] == 'N'): #increase row
						curr[0] = curr[0] -1 
					elif (Is[i] == 'S'): #decrease row
						curr[0] = curr[0] + 1
					elif (Is[i] == 'E'): #increase col
						curr[1] = curr[1] + 1
					elif (Is[i] == 'W'): #decrease col
						curr[1] = curr[1] - 1
				visited.append(curr.copy())

		return curr

T = 1
N = 11
R = 5
C = 8
Sr = 3
Sc = 4
Is = 'NEESSWWNESE'
#print(wiggle(T, N, R, C, Sr, Sc, Is))
#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aac


def main():
	lines = stdin.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].replace('\n', '')

	T = int(lines[0]) #number of tests
	j=1 #the element in which tests  start; 
	    #first element only says how many inputs are in this test

	for i in range(T): #for the number of tests
		pairs = []

		for k in range(j, j+2): #from where curr test inputs starts until the end
								#lines[j] says how many inputs for this test
			pairs.append(lines[k].split()) #read the fruit and value one by one
		sr, sc = solution(pairs)

		#print spaces between tests, excluding last test
		print("Case #{}:".format(i+1), sr, sc)

		#go to next test
		j = j + 2
    


def solution(pairs):

	#pairs[0] = ['5', '3', 6', ...]
	#pairs[1] = ['EEWNS']

	N = int(pairs[0][0])
	s = pairs[1][0]

	curr = [int(pairs[0][3]), int(pairs[0][4])]
	visited = []
	visited.append(curr.copy()) 
		#can't add a list to a hashmap/hashset, has to be in values
		#use a hashset instead #set.add() not append()
		#to keep track of lists, add lists into a list of lists, but use list.copy()

	for letter in s:
		if (letter == 'N'): #increase row
			curr[0] = curr[0] - 1
		elif (letter == 'S'): #decrease row
			curr[0] = curr[0] + 1
		elif (letter == 'E'): #increase col
			curr[1] = curr[1] + 1
		elif (letter == 'W'): # decrease col
			curr[1] = curr[1] - 1

		if curr not in visited:
			visited.append(curr.copy())
		else:
			while curr in visited:
				if (letter == 'N'): #increase row
					curr[0] = curr[0] -1 
				elif (letter == 'S'): #decrease row
					curr[0] = curr[0] + 1
				elif (letter == 'E'): #increase col
					curr[1] = curr[1] + 1
				elif (letter == 'W'): #decrease col
					curr[1] = curr[1] - 1
			visited.append(curr.copy())

	return curr


if __name__ == "__main__":
    main()










