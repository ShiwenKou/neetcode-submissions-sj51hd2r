class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        seenP, seenA = set(), set()

        def dfs(r, c, visited, prevHeight):

            if (r not in range(rows) or c not in range(cols) or (r, c) in visited or
                heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))

            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, seenP, heights[0][c])
            dfs(rows - 1, c, seenA, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, seenP, heights[r][0])
            dfs(r, cols - 1, seenA, heights[r][cols - 1])
        
        return list(seenP.intersection(seenA))