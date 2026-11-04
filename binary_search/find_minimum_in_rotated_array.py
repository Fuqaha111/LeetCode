class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

    
        
        result = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break


            mid = (l+r)//2
            result = min(result, nums[mid])
            ### Left array
            if nums[mid] >= nums[l]:
                l = mid + 1

            ### Right array
            else:
                r = mid - 1
        return result

sol = Solution()
print(sol.findMin([3, 1]))