
class Trie:

	def __init__(self, letter):
		self.value = letter 
		self.children = {}

	def insert(self, s): #s is a string

		for letter in s:
			if(letter in self.children):
				self = self.children[letter]
			else:
				new_node = Trie(letter)
				self.children[letter]= new_node
				self = new_node

		#self.children['*'] = True

	def Print(self):
		print(self.value)

		for child in self.children:
			self.children[child].Print()

def longest_common_prefix(words):

	root = Trie(0)

	for word in words:
		root.insert(word)
	

	if(len(root.children)!=1):
		print("nope")

	while(len(root.children)==1):
		for child in root.children:
			root = root.children[child]
		print(root.value)


words = ["flower", "flow", "floght"]
longest_common_prefix(words)
