class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # res = 0


        # def bfs(r,c):
        #     count = 1
        #     q = collections.deque()
        #     visit.add((r,c))
        #     q.append((r,c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #         for dr,dc in directions:
        #             r,c = row+dr, col+dc
        #             if(r in range(rows) 
        #             and c in range(cols) 
        #             and grid[r][c] == 1 
        #             and (r,c) not in visit):
        #                 q.append((r,c))
        #                 visit.add((r,c))
        #                 count +=1
        #     return count


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r,c) not in visit:
        #             count = bfs(r,c)
        #             res = max(count,res)
        # return res

        #dfs
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if(r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in visit):
                return 0
            
            visit.add((r,c))
            return (1+ dfs(r+1,c)+
                       dfs(r-1,c)+
                       dfs(r,c+1)+
                       dfs(r,c-1))  
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(dfs(r,c), area)
        return area