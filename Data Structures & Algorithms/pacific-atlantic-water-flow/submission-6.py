class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        seenP, seenA = set(), set()


        def dfs(r, c, visit, prev):
            if (r not in range(len(heights)) or c not in range(len(heights[0])) or
                heights[r][c] < prev or (r, c) in visit):
                return
            
            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for r in range(len(heights)):
            dfs(r, 0, seenP, heights[r][0])
            dfs(r, len(heights[0]) - 1, seenA, heights[r][len(heights[0]) - 1])
        
        for c in range(len(heights[0])):
            dfs(0, c, seenP, heights[0][c])
            dfs(len(heights) - 1, c, seenA, heights[len(heights) - 1][c])
        

        return list(list(p) for p in (seenA & seenP))

