class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]

        rank = [1] * n


        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]] # 你的爸爸，是你爸爸的爸爸。linked to graphfather
                res = par[res] #下次我们找你爸爸的爸爸。看看你爸爸的爸爸是不是自己
            return res

        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0 # no union needed
            

            if rank[p1] > rank[p2]: # 我们把p2放到p1下
                par[p2] = p1
                rank[p1] += rank[p2]
            else: # we put p1 under p2
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        total = n
        for n1, n2 in edges:
            total -= union(n1, n2)
        return total