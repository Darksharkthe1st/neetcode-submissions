class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # We perform BFS starting from all the rotting oranges:
        # Pick out the rotten ones into a list
        # Make a new list of their neighbors, rot them
        # Make a new list of those oranges' neighbors, rot them
        # And so on

        def neigh(x, y):
            opts = [(x-1,y),(x, y-1),(x+1,y),(x,y+1)]
            ret = []
            for o in opts:
                if o[0] >= 0 and o[1] >= 0 and o[0] < len(grid) and o[1] < len(grid[o[0]]) and grid[o[0]][o[1]] == 1:
                    ret.append(o)
            return ret

        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        # def show_grid():
        #     for i in range(len(grid)):
        #         print(grid[i])
        #     print("======")

        new_rots = rotten
        rounds = 0
        while new_rots:
            # show_grid()
            rotten = new_rots
            new_rots = []
            for r in rotten:
                new_rots += neigh(r[0],r[1])
            for r in new_rots:
                grid[r[0]][r[1]] = 2
            if new_rots:
                rounds += 1
        
        # show_grid()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return rounds

