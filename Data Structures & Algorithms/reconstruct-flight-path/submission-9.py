class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        # adjList
        adjList = collections.defaultdict(list)

        for n1, n2 in tickets:
            adjList[n1].append(n2)

        
        res = ['JFK']

        def dfs(node):

            # make sure we use every tickets
            if len(res) == len(tickets) + 1: # "JFK" in res so we add one here
                return True


            for i, nei in enumerate(list(adjList[node])):

                adjList[node].pop(i)
                res.append(nei)

                if dfs(nei):
                    return True

                adjList[node].insert(i, nei)
                res.pop()
            
            # if the for loop finishes and the current node doesn't have a nei
            return False # force to backtracking

        dfs('JFK')
        return res