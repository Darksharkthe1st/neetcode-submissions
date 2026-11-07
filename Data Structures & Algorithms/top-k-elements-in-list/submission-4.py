class Solution:
    from collections import heapq


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print("start", k)
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        # print(freqMap)
        mh = []

        for key, v in freqMap.items():
            heapq.heappush(mh, (-v, key))
        
        results = []
        # print(k)
        for i in range(k):
            # print(i, mh, k)
            if not mh:
                break
            priority, task = heapq.heappop(mh)
            results.append(task)
            # print("added")

        return results