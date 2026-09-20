class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def kTime(k, piles):
            hrs = 0
            for p in piles:
                hrs += p // k + (1 if (p % k != 0) else 0)
            return hrs
        
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            # print(k)
            hrs = kTime(k, piles)
            if hrs <= h:
                res = k
                right = k - 1
            else:
                
                left = k + 1
        return res