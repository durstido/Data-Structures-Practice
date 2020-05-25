def lengthOfLongestSubstring(s):
        
    st_ix = 0
    Max = 0
    c_count = 0
    Dict = dict()
    
    for i in range(len(s)):
        if s[i] not in Dict:
            Dict[s[i]] = i
            c_count = c_count + 1
        else:
            if(Dict[s[i]]<st_ix):
                Dict[s[i]] = i
                c_count = c_count + 1
            else:
                if (c_count > Max):
                    Max = c_count
                c_count= i - Dict[s[i]] #dist, including current one
                st_ix = i - c_count + 1
                Dict[s[i]] = i
        if i==len(s)-1:
            if(c_count > Max):
                Max = c_count

    print(Max)

lengthOfLongestSubstring('pwkwwedklwwel') #answer is 5