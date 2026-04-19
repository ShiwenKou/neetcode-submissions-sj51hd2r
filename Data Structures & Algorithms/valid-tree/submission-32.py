class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        par = [i for i in range(n)]

        rank = [1] * n
        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        components = n

        for n1, n2 in edges:
            if union(n1, n2) == False:
                return False
            components -= 1
        return components == 1