import sys

class Node:

	def __init__(self, data): #when you define this, will define value at root
		self.left = None
		self.right = None
		self.parent = None
		self.data = data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data)
		if self.right:
			self.right.PrintTree()

	def PrintTreeIncr(self):

		#print all left first
		if(self.left):
			self.left.PrintTreeIncr()
		
		print(self.data)

		#go to right
		if(self.right):
			self.right.PrintTreeIncr()

	def PrintTreePost(self):

		if(self.left):
			self.left.PrintTreePost()
		if(self.right):
			self.right.PrintTreePost()
		print(self.data) 


	def insert(self, data): #data of new node
		if(data > self.data): #if data of new node is greater than root
			#check that left doesn't have a null -- if it does, insert
			if(self.right==None):
				self.right = Node(data) #create a new node out of this data
				self.right.parent = self
			#go right and recurisvely call this until find correct place
			else:
				self.right.insert(data)
		elif (data < self.data): #if data of new node is less than root
			#check first if left is null -- if it is, then insert there
			if(self.left==None):
				self.left = Node(data)
				self.left.parent = self
			#recurisvely call this with self = self.right
			else:
				self.left.insert(data)

	def search(self,data):
		if(data==self.data):
				return self
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

	def PrintPaths(self):
		if(self.left == None and self.right == None):
			print("new path: from bottom")
			print(self.data)
		if(self.left):
			self.left.PrintPaths()
			print(self.data)
		if(self.right):
			self.right.PrintPaths()
			print(self.data)


	def swap(self):

		if (self == None):
			return

		if(self.left):
			self.left.swap()
		if(self.right):
			self.right.swap()

		tmp=self.right
		self.right = self.left
		self.left= tmp

	def doubleTree(self):

		if (self == None):
			return

		if (self.right):
			self.right.doubleTree()
		if (self.left):
			self.left.doubleTree()

		new_node = Node(self.data)
		new_node.left = self.left 
		self.left = new_node


	def isBST(self):

		if (self == None):
				return True

		if(self.right):
			if(self.right.isBST() == False):
				return False

		if(self.left):
			if(self.left.isBST() == False):
				return False
 
 		if(self.right):
			right_min = self.right.BT_Min()
			if(right_min < self.data):
				return False

		if (self.left):
			left_max = self.left.BT_Max()
			if(left_max>self.data):
				return False

		return True

 
	def BT_Max(self): 

		if (self == None):
			return

		left_max = right_max = 0

		if(self.left):		
			left_max = self.left.BT_Max()
		if(self.right):
			right_max = self.right.BT_Max()

		if (left_max > self.data and left_max > right_max):
			return left_max
		elif (right_max > self.data and right_max > left_max):
			return right_max 
		elif (self.data > right_max and self.data > right_max):
			return self.data
		else:
			return self.data

	def BT_Min(self):

		if (self==None):
			return

		left_min = right_min = sys.maxsize

		if(self.left):
			left_min = self.left.BT_Min()
		if(self.right):
			right_min = self.right.BT_Min()

		if (left_min < self.data and left_min < right_min):
			return left_min
		elif (right_min < self.data and right_min < left_min):
			return right_min
		elif (self.data < right_min and self.data < right_min):
			return self.data
		else:
			return self.data 

	def search_k(self, k):
		#go right k-1
		#go left k-1

		if (k==0):
			print(self.data)
			return

		else:
			if(self.left):
				self.left.search_k(k-1)
			if(self.right):
				self.right.search_k(k-1)


	def remove(self, node_value):
			
			self = search(node_value)

			#one child
			if((self.right and self.left == None) or (self.left and self.right == None)):
					if(self.right):
						if(self.parent.parent): #if grandparent exists
							if(self.parent.parent.right == self.parent):
								self.parent.parent.right = self
							if(self.parent.parent.left == self.parents):
								self.parent.parent.left = self

			#two children
			if(self.right and self.left):


			else: #no children
				if(self.parent.right == self):
					self.parent.right == None
				elif(self.parent.left == self):
					self.parent.left == None






root1 = Node(5)
root1.insert(3)
root1.insert(9)
root1.insert(7)
root1.insert(10)
root1.insert(20)
root1.insert(2)

root2 = Node(5)
root2.insert(3)
root2.insert(9)

wrong_node = Node(7)
root2.left.right = wrong_node


print(root1.search_k(0))

#root.insert(4)
#root.insert(1)
#root.insert(7)
#root.insert(6)
#root.swap()
#print("printing paths")
#root.PrintTreeIncr()
#root.PrintTreePost()
#root.PrintPaths()




