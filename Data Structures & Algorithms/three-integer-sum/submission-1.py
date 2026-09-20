class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort along the length of nums
        triplets: set = set()
        nums.sort()
        # Go through 1 from start to 1 from end:
        soln = []
        print("What time is it")
        for i in range(1, len(nums) - 1):
            l: int = i-1
            r: int = i+1
            print(f"Examining i: {i}")
            while (l >= 0 and r <= len(nums) - 1):
                sum = nums[i] + nums[l] + nums[r]
                if (sum == 0):
                    solution = [nums[l],nums[i],nums[r]]
                    if solution not in soln:
                        soln.append(solution)
                    if (r < len(nums) -1):
                        r +=1
                    else:
                        l -= 1

                elif (sum > 0):
                    l-=1
                else:
                    r+=1

        return soln
