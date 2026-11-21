class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # In order for this to work, we need an acyclic graph
        # How do we check for an acyclic graph?
        # Find a node which has no prereqs (if none, then false)
        # DFS on it
        # Have a set of nodes in your stack
        # If you encounter a node that pts back to the growing stack, you have a cycle
        # Do this until you've DFS'd all completed sections of the graph
        all_visited = set()
        graph = {}
        focus = set()
        no_req = set()
        fully_visited = set()

        # print("ran")
        # First, make an adj. list
        for p in prerequisites:
            if p[0] not in focus:
                no_req.add(p[0])
                focus.add(p[0])
            focus.add(p[1])
            no_req.discard(p[1])
            
            graph[p[0]] = graph.get(p[0], [])
            graph[p[0]].append(p[1])


        # print(graph)
        # print(no_req)
        for n in no_req:
            curr_visit = set()
            def dfs(n):
                # print("c",curr_visit, n)
                if n in curr_visit:
                    # print("fired", n)
                    return False
                if n in all_visited:
                    return True
                curr_visit.add(n)
                all_visited.add(n)
                for neigh in graph.get(n, []):
                    if not dfs(neigh):
                        return False
                # print("Good", n)
                curr_visit.discard(n)
                return True
            value = dfs(n)
            # print("D", value)
            if not value:
                # print("also fired")
                return False
        

        
        return len(focus) == len(all_visited)


