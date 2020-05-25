class Trie:

	def __init__(self, letter):
		self.letter = letter
		self.children = dict() 
		self.count = 0 #how many times it's been used
		self.Max_letter = None

	def insert(self, word):
		for letter in word:
			if(letter in self.children):
				self = self.children[letter]
				self.count += 1
			else:
				temp = Trie(letter)
				self.children[letter] = temp
				self = temp
				self.count += 1
		#self.children['*'] = True


	def Print(self):
		print(self.letter)
		for child in self.children: #for however many words with current and this specific next letter
			if(child=='*'):
				break
			self.children[child].Print()

	def search(self,word):
		for letter in word:
			if(letter in self.children):
				self = self.children[letter]
			else:
				print("nope")
				break

		#found it if: last charcter is leaf (has * =T), and this last character isn't null  

	def max_depth(self): #find a string with k chars
		arr={}
		depth = 0
		if (self.children=={}):
			return depth
		else: 
			depth +=1 
			for letter in self.children:
				arr[letter] = self.children[letter].max_depth()

		Max = 0
		for letter in self.children:
			if (arr[letter] > Max):
				Max = arr[letter]
				self.Max_letter = letter
		depth += Max

		return depth

	def print_longest(self):

		if(self.children=={}):
			return 

		print(letter)
		max_depth(self)
		print(self.Max_letter)





		return -1

	#def search_k(self,word): #find longest string with at most 



root = Trie(None)
root.insert("pet")
root.insert("pel")
root.insert("pelloo")
#print(root.children['p'])
#root.Print()
root.search("pel")
print(root.max_depth())
