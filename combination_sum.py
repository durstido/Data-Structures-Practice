
class Sol:

	def __init__(self):
		self.op_count = 0

	#counting number of sets in solutions recursively
	def count_rec(self,S,n): #S is set of candidates/ all the coins we have, n is our target some
		coins = self.helper(S,n,len(S)-1,0)
		return coins, self.op_count

	def helper(self,S,n,m,count): #m is location we're looking at
		self.op_count += 1
		if(n==0): #one solution -- we have no money, so exactly one way to solve the problem: choose nothing
			print(count) #how many coins in this iteration
			return 1
		elif (n<0 or m<0): #either negative sum of money we're looking for, or finished our array
			return 0

		return self.helper(S,n-S[m],m,count+1) + self.helper(S[:m],n,m-1,count)  #--> S[:2] will only have S[0], S[1]
		#two options:
			#we either use the current value at least once, which means we're looking for the target-element, including current value (that's why m=m)
			#or we dont use that value, then we're looking for the same, but with the array minus the last element


	#count number of sets in solutions iteratively 
	def iter_count1(self, S, n): #S is array of possible coins, m is len of S (how many coins), n is target
		#m = number of possible coins
		m=len(S)
		#decalre a 2D table, with target+1 cells, and each cell having m cells (one per each coin)
		table = [[0 for x in range(m)] for x in range(n+1)] 

		for i in range(m):
			table[0][i] = 1 #initialize all coins under 0 to have 1; should technically be 0,
							#but then later, instead of doing count = table[new_t] + 1 will just do count = table[new_t]

		for i in range(1,n+1):		#for each cell in arr
			for j in range(m): 		#for each coin

				#First thing, try using this coin (only if possible): Then, get a new target = curr target (i) - coin
				new_t = i - S[j]
				count_using_j = 0
				if (new_t >= 0):
					#Then, wee how many coins we had to use to get to that new target (dont +1, since t[0]=1)
					#but remember, only check the new target @ cell of curr coin, to not have to iterate over all coins at that new target
					count_using_j = table[new_t][j]

				#Now, say we don't use this coin. Then, we need to look up at row above (if possible) to see
				#how many combinations we needed to get to curr target using up to (not including) curr coin
				count_excluding_j = 0
				if (j>0):
					count_excluding_j = table[i][j-1] #row, col --> staying on curr col (same curr target), just row above

				#over count for curr target and curr coin both above together
				count = count_using_j + count_excluding_j
				#place is in the table
				table[i][j] = count

		#we want to return the last col (our actual target)'s last cell, since that holds the number of combinations
		#to get to our target using all coins up to and including last coin
		return table[n][m-1]

	#count number of sets in solutions iteratively 
	def iter_count2(self, S, n): #S is array of possible coins, m is len of S (how many coins), n is target
		#decalre a 2D table, with target+1 cells, and each cell having m cells (one per each coin)
		table = [0 for x in range(n+1)] 

		table[0] = 1

		for coin in S:							#for every possible coin
			for new_target in range(n-coin+1): 	#for all possible target combinations from 0 to n-coin (+1 cuz 0-indexing)
				table[new_target+coin] = table[new_target+coin] + table[new_target] 
				#for each new coin we're looking at, we want to have however many combinations we found before + this new possible ones
		return table[n]

	#return all sets in solution itertively 
	def combination_sum1(self, S, n):
		table = [set() for x in range(n+1)]  #create a set for each one

		print(table[0].add(()))				 #have an empty array in the first set (so that when called, can actually use it; when calling a set, if nothing is in it, it basically doesn't exist)

		for coin in S:
			for new_target in range(n-coin+1): 		#for all possible new_targets using this coin
				table[new_target + coin] |= {paths_at_new_target + (coin,) for paths_at_new_target in table[new_target]} #{} is a set
				#at each table[new_target+coin], we want to loop over all possible paths at table[new_target] and add curernt coin
				#and also, we want to keep whatever other paths we had until now
				#to combine sets a = a|b (their union) or simply a |= b
		return list(table[n])	#instead of it being a set, we'll return it as a list/array



	#will return the same solution multiple times, but it works
	def combination_sum2_rec(self, S,n):

		solution=[]
		stack=[]

		def helper(S,n,m,stack):
			print(S,n,m,stack)
			if(n==0):
				solution.append(list(stack))
				return

			if(n<0 or m==0):
				return


			stack_new = list(stack)
			stack_new.append(S[m-1])
			helper(S[:m-1], n-S[m-1], m-1, stack_new) #either you're using it once
			helper(S[:m-1], n, m-1, stack)	#or you don't use it at all
			#can't do S-S[m-1]

		helper(S,n,len(S), stack)
		return solution

	def combination_sum2_iter(self, S, n):
		#in this case, we have to sort them.
		#if we had 1,3,1, we'd have: 
			#coin=1, [{()}, {(1,)}, set(), set(), set()]
			#coin=3, [{()}, {(1,)}, set(), {(3,)}, {(1, 3)}]
			#coin =1,[{()}, {(1,)}, {(1, 1)}, {(3,)}, {(1, 3), (3, 1)}]
		#with 1,1,3 however we'd have:
			#[{()}, {(1,)}, set(), set(), set()]
			#[{()}, {(1,)}, {(1, 1)}, set(), set()]
			#[{()}, {(1,)}, {(1, 1)}, {(3,)}, {(1, 3)}]
		S.sort()
		table = [set() for x in range(n+1)]  #create a set for each one

		table[0].add(())				 #have an empty array in the first set (so that when called, can actually use it; when calling a set, if nothing is in it, it basically doesn't exist)

		for coin in S:
			#for new_target in reversed(range(n-coin+1)): 		#for all possible new_targets using this coin
			for new_target in reversed(range(n-coin+1)):
				table[new_target + coin] |= {paths_at_new_target + (coin,) for paths_at_new_target in table[new_target]} #{} is a set
				#this time, we're going to go backwards:
				#say coin=2, n=6. Our highest new_target would be 5, so we'll start at 5 and add to 7 all previous + 2 (nothing, 5 is set)
				#we'll keep going down until n=0. Then, we'll add to n=2 {(2,)}. So now we only used 2 once.
				#for another coin=2, n=6, when we reach n=2, we'll do target[n=4] = @2 + (,2) = {(2,2)}, so again we only used it once
				#this way, we only use a coin once
		return list(table[n])	#instead of it being a set, we'll return it as a list/arrays

n = 8
S = [10,1,2,7,6,1,5]
#n=6
#S = [2,2,2,3,3]
ob = Sol()
print(ob.combination_sum2_iter(S,n))



