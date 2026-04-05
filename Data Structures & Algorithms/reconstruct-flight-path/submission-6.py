class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # this problem we should use backtracking. if one path(solution) hits the base case
        #(where curr node has no more neighbors, which len(seen) != n). we need to backtrack

        tickets.sort()
        adjList = collections.defaultdict(list)
        for n1, n2 in tickets:
            adjList[n1].append(n2)
        
        res = ['JFK']
        def dfs(node):

            if len(res) == len(tickets) + 1:
                return True
            # if adjList[node] == []:
            #     return False



            for i, nei in enumerate(list(adjList[node])): # remove links

                adjList[node].pop(i)
                res.append(nei)

                if dfs(nei):
                    return True
                # if not hit the base case
                res.pop()
                adjList[node].insert(i, nei)
            return False
        dfs('JFK')
        return res
