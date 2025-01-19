from collections import Counter


s, t = "egg", "add"

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t): 
            return False

        mapper = {} 

        for i in range(len(s)):
            if s[i] in mapper:
                if mapper[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapper.values():
                    return False
                mapper[s[i]] = t[i]
        
        return True
    
res = Solution.isIsomorphic(Solution, s, t)
print(res)


        
        