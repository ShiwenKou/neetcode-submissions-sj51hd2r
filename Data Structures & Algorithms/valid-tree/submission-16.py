class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # this is a undirect problem so we can use union-find to detect loops

        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False # loop detected
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        total = n
        for n1, n2 in edges:
            total -= 1
            if union(n1, n2) == False:
                return False
        
        if total == 1:
            return True
        else:
            return False