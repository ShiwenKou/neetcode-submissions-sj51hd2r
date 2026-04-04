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
            if node not in adjList: # have node unvisited while no path, return for backtracking
                return False
            
            for i, nei in enumerate(list(adjList[node])):

                res.append(nei)
                adjList[node].pop(i)

                if dfs(nei):
                    return True # no need exploring
                
                res.pop()
                adjList[node].insert(i, nei)
        dfs('JFK')
        return res

