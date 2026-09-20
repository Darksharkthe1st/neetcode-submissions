class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen: dict = {}
        # for i in range(len(numbers)):
        #     if (target-numbers[i] in seen):
        #         return [seen[target-numbers[i]]+1, i + 1]
        #     else:
        #         seen[numbers[i]] = i
        # return [-1,-1]
        i = 0
        j = len(numbers) - 1
        sume = 0

        while (i < j):
            sume = numbers[i] + numbers[j]
            if (sume == target):
                return [i+1, j+1];
            elif sume < target:
                i += 1
            else:
                j -= 1
        
        return [-1, -1]
