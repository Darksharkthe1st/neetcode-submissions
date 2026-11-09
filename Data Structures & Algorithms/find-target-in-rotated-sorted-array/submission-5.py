class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Trivial O(n) soln:
        # Rotate manually, then do Bin Search
        rot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rot = i
        
        i = rot
        j = rot + len(nums) - 1
        print("START", rot, i, j)

        def index(i):
            return nums[i % len(nums)]

        while i <= j:
            mid = (i + j) // 2
            v = index(mid)
            print(i, j, mid, v)
            if v == target:
                return mid % len(nums)
            if v < target:
                i = mid + 1
            else:
                j = mid - 1
        
        return -1
