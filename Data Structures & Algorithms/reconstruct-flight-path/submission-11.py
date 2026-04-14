class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        res = ['JFK']
        adjList = collections.defaultdict(list)
        for n1, n2 in tickets:
            adjList[n1].append(n2)

        
        def dfs(node):

            if len(res) == len(tickets) + 1:
                return True

            if adjList[node] == []:
                return False # backtracking

            
            for i, nei in enumerate(list(adjList[node])):

                adjList[node].pop(i)
                res.append(nei)

                if dfs(nei):
                    return True
                res.pop()
                adjList[node].insert(i, nei)


        if dfs('JFK'):
            return res