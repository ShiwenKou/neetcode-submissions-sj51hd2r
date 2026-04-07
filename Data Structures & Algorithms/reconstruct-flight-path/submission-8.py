class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        adjList = collections.defaultdict(list)

        for n1, n2 in tickets:
            adjList[n1].append(n2)

        
        res = []
        res.append('JFK')
        seen = set()
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True # if we don't see all the tickets, we force the if dfs(nei) to miss, and do backtracking

            for i, nei in enumerate(list(adjList[node])):

                adjList[node].pop(i)
                # seen.add(nei)
                res.append(nei)

                if dfs(nei):
                    return True

                res.pop()
                # seen.remove(nei)
                adjList[node].insert(i, nei)
        dfs('JFK')
        return res
