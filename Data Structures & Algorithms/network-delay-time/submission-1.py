class Solution:
    from collections import heapq
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We use Dijkstra's Algo to solve this problem:
        class Node:
            def __init__(self, number, weight):
                self.num = number
                self.weight = weight

            def __lt__(self, o):
                if self.weight == -1:
                    return False
                if o.weight == -1:
                    return True
                return self.weight < o.weight

            def __str__(self):
                return f"({self.num}, {self.weight})"
            
            def __repr__(self):
                return f"({self.num}, {self.weight})"
        # Make the adj list map:
        graph = {}
        # edges = {}
        for t in times:
            graph[t[0]] = graph.get(t[0], [])
            graph[t[0]].append((t[1], t[2]))
            # edges[(t[0], t[1])] = t[2]

        
        
        # Set up pq + weights tracker
        pq = []
        weights = {}
        for i in range(1, n+1):
            weights[i] = -1

        # Now we do dijkstra's algorithm
        heapq.heappush(pq, Node(k, 0))
        checked = 0
        maxtime = 0
        visited = set()

        # print(graph)
        weights[k] = 0
        
        while checked < n and pq:
            curr = heapq.heappop(pq)
            # print(pq, curr)
            if curr.num in visited:
                continue
            
            checked += 1
            visited.add(curr.num)
            if curr.weight > maxtime:
                maxtime = curr.weight
            
            neighbors = graph.get(curr.num, [])
            for e in neighbors:
                new_weight = weights[curr.num] + e[1]
                
                if new_weight < weights[e[0]] or weights[e[0]] == -1:
                    weights[e[0]] = new_weight
                    heapq.heappush(pq, Node(e[0], new_weight))
        

        return maxtime if checked == n else -1
