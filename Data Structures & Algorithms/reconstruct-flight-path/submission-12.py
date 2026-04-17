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
            

            for i, nei in list(enumerate(adjList[node])):
                adjList[node].pop(i)
                res.append(nei)

                if dfs(nei): # 如果有路就不需要backtracking
                    return True

                res.pop()
                adjList[node].insert(i, nei)
            # 如果没路了
            return False # go backtracking

        dfs("JFK")

        return res