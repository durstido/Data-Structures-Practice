class minHeap:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

	def initialize(self):
		self.left = minHeap(50)
		self.left.parent = self
		self.right = minHeap(7)
		self.right.parent = self

	def insert(self, data):

		#find rightmost element
		while(self.right!=None):
			self = self.right

		#adding element
		self.right = minHeap(data)
		self.right.parent = self
		self = self.right #now "self" is the new node we entered

		#propogate element back until find apporpriate location
		while(self.data < self.parent.data):
			tmp_right = self.right
			tmp_parent = self.parent

			self.parent = self.parent.parent
			self.right = self.parent

			tmp_parent.parent = self
			tmp_parent.right = tmp_right

	def Print(self):
		if(self.left):
			self.left.Print()
		print(self.data)
		if(self.right):
			self.right.Print()


heap = minHeap(4)
heap.initialize()
#heap.Print()
heap.insert(2)
heap.Print()







