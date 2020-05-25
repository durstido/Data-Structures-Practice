import math

def replacing_int(N,K):
	m = math.floor(N/K)
	s = N - m*K
	if (s > abs(s-K)):
		s = abs(s-K)
	return s

print(replacing_int(1000000,6))

#keep track of variables
#math/abs