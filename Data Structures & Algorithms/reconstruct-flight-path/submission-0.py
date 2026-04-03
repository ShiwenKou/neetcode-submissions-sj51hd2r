class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = collections.defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adjList[src].append(dst)
        res = ['JFK']
        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True
            if curr not in adjList:
                return False

            for i, v in enumerate(list(adjList[curr])):
                res.append(v)
                adjList[curr].pop(i)

                if dfs(v):
                    return True
                res.pop()
                adjList[curr].insert(i, v)
        dfs('JFK')
        return res