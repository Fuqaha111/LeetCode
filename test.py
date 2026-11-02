class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        counts1 = {}
        for char in t:
            if char in counts1:
                counts1[char] += 1
            else:
                counts1[char] = 1
        
        if counts.items() == counts1.items():
            return True
        return False
    
sol = Solution()
result = sol.isAnagram("cat", "rat")
print(result)