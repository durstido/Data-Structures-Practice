

class Queue:

	def __init__(self):
		self.queue = []

	def read(self):
		value = self.queue[0]
		self.queue = self.queue[1:]
		return value

	def write(self, value):
		self.queue.append(value)

	def Print(self):
		for element in self.queue:
			print element


queue = Queue()
queue.write(0)
queue.write(5)
queue.write(15)
queue.Print()
print(queue.read())
print("after popping")
queue.write(20)
queue.Print()