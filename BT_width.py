class Node:


	def __init__(self, data): #when you define this, will define value at root
		self.left = None
		self.right = None
		self.data = data

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


def width(root):

	left_l = left_r = right_l = right_r = 0 #in case there is no left or right

	if (root.left):
		someroot, left_l, left_r = helper(root.left, -1, 0) #root, leftmost, rightmost
	if(root.right):
		someroot, right_l, right_r = helper(root.right, 0, 1)



	#choose left most
	if (left_l < right_l):
		left_index = left_l
	else:
		left_index = right_l

	if(left_r > right_r):
		right_index = left_r
	else:
		right_index = right_r

	print(left_index)
	print(right_index)
	width = -(left_index) + right_index
	
	return width


def helper(root, leftmost, rightmost):
	MaxL = left_l = right_l = leftmost
	MaxR = left_r = right_r = rightmost

	if(root.left):
		someroot, left_l, left_r = helper(root.left, leftmost-1, rightmost)
	if(root.right):
		someroot, right_l, right_r = helper(root.right, leftmost, rightmost+1)

	if(left_l < right_l):
		MaxL = left_l
	else: 
		MaxL = right_l

	if(left_r>right_r):
		MaxR = left_r
	else: 
		MaxR = right_r 

	return root, MaxL, MaxR




root = Node(1)
root.insert_left(2)
root.left.insert_right(3)
root.left.insert_left(7)
root.left.right.insert_right(4)
root.left.right.right.insert_right(5)
root.left.right.right.right.insert_right(6)

print("width", width(root))
