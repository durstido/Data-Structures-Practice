class Node:


	def __init__(self, data): #when you define this, will define value at root
		self.left = None
		self.right = None
		self.data = data
		self.Count = 0
		self.MaxDepth=0

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data)
		if self.right:
			self.right.PrintTree()


	def insert_right(self, data):
		if(self.right == None): #then you can insert
			self.right = Node(data)

	def insert_left(self,data):
		if(self.left == None):
			self.left = Node(data)

	def search(self,data):
		if(data==self.data):
				print("found")
		elif(data > self.data):
			if(self.right==None):
				print("does not exist")
			else: #go right and recurse on this
				self.right.search(data)
		elif(data < self.data):
			if(self.left==None):
				print("does not exist")
			else: #go left and recurse
				self.left.search(data)

	def count(self):
		#count to left
		if(self.left):
			self.Count += self.left.count()
		#count to right
		if(self.right):
			self.Count += self.right.count()

		#add both and 1 to itself
		self.Count += 1

		return self.Count

	def maxDepth(self):
		#see if there is a next level, and add 1
		if(self.left == None and self.right == None):
			return 0

		#if not, add 1 for current level
		self.MaxDepth += 1
		left_max=0
		right_max=0

		if(self.left):
			left_max = self.left.maxDepth()
		if(self.right):
			right_max = self.right.maxDepth()

		if (left_max > right_max):
			self.MaxDepth += left_max
		else:
			self.MaxDepth += right_max

		return self.MaxDepth

	def equal(self, sec_tree):

		if(sec_tree == None):
			if(self == None):
				return
			else:
				print("nope from if")
				return

		if(self.data == sec_tree.data):
			if(self.left):
				self.left.equal(sec_tree.left)
			if(self.right):
				self.right.equal(sec_tree.right)
		else:
			print("nope from else")
			return

	def LCA(self, n1, n2):

		if(self==None):
			return

		if(self.data==n1 or self.data==n2):
			return self.data

		isleft=isright=False

		if(self.left):
			isleft = self.left.LCA(n1,n2)
		elif(self.left):
			isright = self.right.LCA(n1,n2)

		if(isleft and isright):
			return self.data
		if(isleft and isright==None):
			return isleft
		if(isright and isleft==None):
			return isright
		else:
			return




root1 = Node(2)
root1.insert_left(1)
root1.insert_right(3)
root1.left.insert_left(4)
root1.right.insert_right(10)

root2 = Node(2)
root2.insert_left(1)
root2.insert_right(3)
root2.left.insert_left(4)
root2.right.insert_right(9)

#print("count (number of nodes)", root.count())
#root1.equal(root2)
#print(root1.MaxDepth())

root3 = Node(1)
root3.insert_left(2)
root3.left.insert_right(5)
root3.left.insert_left(4)
print(root3.LCA(4,5))




