class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(x, y):
            neigh = [(x,y-1), (x-1,y),(x+1,y), (x,y+1)]
            res = []
            for n in neigh:
                if n[0] < 0 or n[1] < 0 or n[0] > (len(grid) - 1) or n[1] > (len(grid[0]) - 1):
                    continue
                if grid[n[0]][n[1]] != '1':
                    continue
                res.append(n)
            return res
            

            
        def bfs(startX, startY):
            if grid[startX][startY] != '1':
                return 0
            toVisit = [(startX, startY)]
            visited = set()
            while toVisit:
                curr = toVisit.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                grid[curr[0]][curr[1]] = '-1'
                toVisit += neighbors(curr[0], curr[1])

            return 1

        def show_grid():
            for i in range(len(grid)):
                print(grid[i])

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count += bfs(i, j)
                # print("COUNT:", count)
                # show_grid()
        
        return count
        
