class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = {}

        for i in nums:
            if i in seen:
                return True
            seen[i] = "seen"
        return False
    
        """
        if len(nums) != len(set(nums)):
            return False
        return True
        """
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))