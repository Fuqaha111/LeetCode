class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)

        while l <= r:
            mid = (l + r) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess > target:
                r = mid - 1
                
            else:
                l = mid + 1

sol = Solution() 
print(sol.search([2, 3, 4, 5, 7, 9, 100, 102, 110], 7))         