class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()


        adjList = collections.defaultdict(list)

        for n1, n2 in tickets:
            adjList[n1].append(n2)

        

        res = ['JFK']

        
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            
            if node not in adjList:
                return False
            
            for i, nei in enumerate(list(adjList[node])):

                adjList[node].pop(i)
                res.append(nei)

                if dfs(nei): return True

                adjList[node].insert(i, nei)
                res.pop()
            return False

        dfs('JFK')
        return res