class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        



        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1): # find parent

            if n1 != par[n1]:
                par[n1] = find(par[n1]) # 1<-2 . node 2's parent is not itself. we find node 1's parent
            return par[n1]
        
        # 1<-2<-3 3's parent is not itself, par[3] = 1
        # frame 2, we sent 2 in, 2's parent not itself par[2] = 1 return 1
        # frame 3, we sent 1 in, 1's parent is itself. return 1 back

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        total = n
        for n1, n2 in edges:
            total -= union(n1, n2)
        return total