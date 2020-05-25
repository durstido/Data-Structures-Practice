
from collections import deque


def rpn(arr):

	if(arr==None):
		return None
	
	stack = deque()
	for element in arr: 
		if (element=='*' or element=='+' or element=='/' or element=='-'):
			if(stack):
				value = stack.pop()
				if(element=='*'):
					value = value * stack.pop() 
				elif(element=='+'):
					value = value + stack.pop() 
				elif(element=='-'): 
					value = value - stack.pop() 
				elif(element=='/'): 
					value = value / stack.pop() 
				stack.append(value) 

		else: #value is a number
			number = int(element)
			stack.append(number)

	return stack.pop()

arr = ["2", "3", "+", "4", "3", "-", "*"]
# (2+3) * (3-4)
print(rpn(arr))