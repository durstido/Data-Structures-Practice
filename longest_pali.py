def long_pali(s):

	Dict = {}
	Max = 0
	cpl = 0 #current poli length

	for i in range(len(s)):
		print(s[i])

		#haven't seen letter before
		if s[i] not in Dict.values():
			Dict[i] = s[i]

		#have seen letter before
		else:

			#currently adding to poli
			if (cpl>1):
				if(Dict[i-cpl-1] == s[i]): #cpl=2 or more (we're creating poli), "open paranthese"
					cpl = cpl + 2
					print("here", cpl)
				#elif(Dict[i-cpl] == s[i]):
				#	cpl = cpl + 1
			#currently creating poli
			elif(Dict[i-1] == s[i]):
				cpl = 2
			elif(Dict[i-2] == s[i]):
				cpl = 3
			#have seen letter before, but not apart of current poli or a new poli
			else:
				cpl = 0
			Dict[i] = s[i]

			if (cpl > Max):
				print(cpl)
				Max = cpl

	print(Max)

long_pali("dcbcbccccc")
