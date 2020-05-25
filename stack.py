from collections import deque

class Stack:

	def __init__(self):
		self.stack = deque()

	def insert(self, value):
		self.stack.append(value)

	def pop(self):
		return self.stack.pop()

	def print_stack(self):
		print(self.stack)

	def peek(self):
		print(self.stack[len(self.stack)-1])


def fib_using_stack(n):
	st = Stack()
	i=0
	st.insert(1)
	st.insert(1)
	while (i<n):
		fib_n_1 = st.pop()
		fib_n_2 = st.pop()
		st.insert(fib_n_1) #the n-2 for next time
		fib_n = fib_n_1 + fib_n_2 
		st.insert(fib_n) #the n-1 for next time
		i = i + 1
	print(fib_n)


st = Stack()
st.insert(0)
st.insert(1)
st.insert(2)
fib_using_stack(6)