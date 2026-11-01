"""
- create an empty list called seen
- create a loop that goes through each element in the list while keeping track of the index
- create a variable called complement that is equal to target - n
- check if complement is in seen  - if yes return complemnt[i] and current n[i] in the list
-                                 - if not add the n and its index to seen
- loop until you passed through all elements in the list

time complexity = o(n) as you need to loop through the function only once at the most and hence teh value is stored in a hash map the lookup us o(1)
space comlexity = o(n) to store the dect seen
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seen:
                return [seen[difference], i]

            else:
                seen[n] = i

sol = Solution()
print(sol.twoSum([15, 11, 2, 7, 10], 9)) 
