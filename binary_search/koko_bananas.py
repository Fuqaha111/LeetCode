import math as m
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
       
    
        l, r = 1 , max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += m.ceil(p/k)

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            
    
    





sol = Solution()

print(sol.minEatingSpeed([2, 3, 5, 1], 5))