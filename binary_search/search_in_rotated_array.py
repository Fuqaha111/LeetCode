class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) -1


        while l <= r:
            mid = (l + r)//2


            if target == nums[mid]:
                return mid
  

            if nums[mid] >= nums[l]:
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1        

        return -1
                

sol = Solution()

print (sol.search([4,5,6,7,0,1,2], 2))