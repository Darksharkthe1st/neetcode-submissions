class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        tempIdxs = []
        output = []

        for i in range(len(temperatures)):
            output.append(0)
            while (len(tempStack) > 0 and temperatures[i] > tempStack[-1]):
                output[tempIdxs[-1]] = i - tempIdxs[-1]
                tempIdxs.pop()
                tempStack.pop()

            tempStack.append(temperatures[i])
            tempIdxs.append(i)

        return output 