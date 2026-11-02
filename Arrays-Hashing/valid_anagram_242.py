"""
Create two hashmaps that store the number of time each letter occurs and loop through one of them to check its the same for the other
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        letters_s = {}
        letters_t = {}

        for i in range(len(s)):
            letters_s[s[i]] = letters_s.get(s[i], 0) + 1
            letters_t[t[i]] = letters_t.get(t[i], 0) + 1


        for letter in s:
            if letters_s[letter] != letters_t.get(letter, 0):
                return False

       
        """""
        if letters_s.items() != letters_t.items():
            return False
        """""
        return True
        
sol = Solution()

assert sol.isAnagram("anagram", "nagaram") == True
assert sol.isAnagram("rat", "car") == False
assert sol.isAnagram("a", "ab") == False      # different lengths
assert sol.isAnagram("ab", "ac") == False     # letter missing from t
assert sol.isAnagram("", "") == True          # empty strings

print("All tests passed!")




