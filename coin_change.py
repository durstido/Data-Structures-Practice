
import sys
class Sol:
	def __init__(self):
		self.op_count = 0

	#count min using recursion
	def count_min_rec(self,S,n): #S is set of candidates/ all the coins we have, n is our target some
		min_coin = self.helper(S,n,len(S)-1,0)
		return min_coin

	def helper(self,S,n,m,count): #m is location we're looking at
		if(n==0): #one solution -- we have no money, so exactly one way to solve the problem: choose nothing
			return count
		elif (n<0 or m<0): #either negative sum of money we're looking for, or finished our array
			return -1

		result_left = self.helper(S,n-S[m],m,count+1)
		result_right = self.helper(S[:m],n,m-1,count)  

		if(result_left==-1 and result_right==-1):
			return -1
		elif(result_left==-1):
			return result_right
		elif(result_right==-1):
			return result_left
		else:
			return min(result_left, result_right)

	#count min using iterative method
	def count_min_iter(self, S, n): #return the minimum number of coins to use in a combination to get the target
		#time: O(n * m) = target*number of coins
			#for i=1:n, for j=0:m (at each cell in arr, try at max all coins possibilties)

		m = len(S)
		table = [float('inf') for x in range(n+1)]	#initialize each element to a super high value 
		#^ will never interfere in the future. Even if some combination leads to this, the other options
		#it has will be less than this, so we'll never actually use this value

		table[0] = 0

		for i in range(1, n+1): 	#for every index in arr/for every n leading up to target
			for j in range(m): 		#for every possible coin 
				#check against every single coin
				if (i-S[j] >=0): 	#if curr target-coin>=0 (we can use that coin)
					new_target = i-S[j] #we're using this coin as our last coin, so what's our new target?
					#given this new target, we want to see how many coins we had to use to get to that
					#then, since we used a coin, we want to add +1 to that
					curr_count = table[new_target] + 1

					#the count will be the minimum of all possible combinations for this target
					table[i] = min(curr_count, table[i])

		return table[n] if table[n] != float('inf') else -1 	#in case we weren't able to create any combination
													#our result will be m+1 as we intiailized, so return -1
													#won't work for everything


n = 11
S = [1,2,5]
ob = Sol()
print(ob.count_min_rec(S,n))



