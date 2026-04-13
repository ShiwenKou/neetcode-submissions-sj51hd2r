class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        setA, setP = set(), set()

        def dfs(r, c, visited, prev):
            if (r not in range(len(heights)) or c not in range(len(heights[0])) or (r, c) in visited or
                heights[r][c] < prev):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    dfs(r, c, setP, heights[r][c])
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    dfs(r, c, setA, heights[r][c])
        
        return [list(pair) for pair in setA.intersection(setP)]