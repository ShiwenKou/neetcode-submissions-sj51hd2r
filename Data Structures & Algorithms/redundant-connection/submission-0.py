class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:



        par = [i for i in range(len(edges) + 1)]

        rank  = [1] * (len(edges) + 1)

        def find(res):
            if res != par[res]:
                par[res] = find(par[res])
            return par[res] # suppose we have 1<- 2. we find 2's parent is not 2, so we 
            # recursively find 2's parent, which is 1's parent. then we find, 1's parent is itself.
            # so we return 1 back. and make par[2] = 1 and return 1.


            # another exmaple. suppose we have 1<-2<-3. we find 3's parent is not 3, so we recursively find 2's parent.
            # in frame 2, 2's parent still not itself. so in frame 3, we find 1's parent. and 1's parent is itself, so we return 1 as our basecase
            # and make 1<-2. we return 1 back to frame 1. and we do 1<-3.
    
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:# attach p2 to p1
                par[p2] = p1
                rank[p1] += rank[p2]
            else: # attach p1 tp p2
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if union(n1, n2) == False:
                return [n1, n2]

        