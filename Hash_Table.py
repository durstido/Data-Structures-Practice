from sets import Set
class Node:

	def __init__(self, key):
		self.next = None
		self.key = key

class Hash:

	def __init__(self):
		self.size = 3 #table size
		self.table = {}

	def hash(self, key):
		return key % self.size #key = reminder when divided by table size 

	def insert(self, key):
		hash_key = self.hash(key)
		if(hash_key in self.table): #then, use the linked list method
			current_node = self.table[hash_key]
			while(current_node.next!=None):
				current_node = current_node.next
			current_node.next = Node(key)
		else:
			self.table[hash_key] = Node(key)

	def search(self, key):
		hash_key = self.hash(key)
		if hash_key in self.table:
			current_node = self.table[hash_key]
			while(current_node.key!=key):
				current_node = current_node.next
			if(current_node.key==key):
				print("found!", current_node.key)
		else:
			print("not found")

	def remove(self, key):
		hash_key = self.hash(key)

		if hash_key in self.table:
			current_node = self.table[hash_key]

			#check current node
			if(current_node.key == key):
				if(current_node.next):
					self.table[hash_key]=current_node.next
					return True
				else:
					self.table[hash_key]=None
					return True

			#if its any other node
			while(current_node.next!=None):
				if(current_node.next.key == key): #if the next one has the key
					if(current_node.next.next):	#make sure next next one exists
						current_node.next = current_node.next.next
						return True
					else: #point to null
						current_node.next = None
						return True
				current_node = current_node.next

		return False

class HashSet:

	def __init__(self):
		self.set = Set()

	def insert(self, value):
		self.set.add(value)


hash_t = Hash()
#print(hash_t.insert(5))
#print(hash_t.insert(6))
#print(hash_t.insert(3))
hash_t.insert(5)
hash_t.insert(3)
hash_t.insert(6)
hash_t.insert(9)
#print(hash_t.table[0].next.key)
#print(hash_t.remove(6))
#print(hash_t.table[0].key)
#print(hash_t.remove(9))
#print(hash_t.table[0].next)

hash_s = HashSet()
hash_s.insert(4)
hash_s.insert(5)
print(hash_s.set)




