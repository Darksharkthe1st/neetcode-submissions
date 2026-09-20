class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def kTime(k, piles):
            hrs = 0
            for p in piles:
                if p < k:
                    hrs += 1
                else:
                    hrs += p // k + (1 if (p % k != 0) else 0)
            return hrs
        
        left = 1
        right = max(piles)
        while left <= right:
            k = (left + right) // 2
            # print(k)
            hrs = kTime(k, piles)
            if hrs > h:
                left = k + 1
                if left == right:
                    continue
            else:
                right = k
            if left == right:
                break
                
        return k