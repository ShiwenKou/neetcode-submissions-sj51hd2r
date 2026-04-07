class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # each char is a node
        adjList = {c:set() for word in words for c in word}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLength = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ''

            for j in range(minLength):
                c1 = word1[j]
                c2 = word2[j]
                if c1 != c2:
                    adjList[c1].add(c2) # each word is a node, we build the adjlist
                    break
        
        # once we have the graph, we want the traverse order of the graph. however, if a->e and a->c->e
        # we may mess up the order, if do this preorder traverse, we can do a postorder traverse and reverse it

        # this is a directed graph, each node has 3 status

        cycle = set() #visiting
        seen = set() #visited
        res = []
        def dfs(node):
            if node in cycle:
                return False
            if node in seen:
                return True
            cycle.add(node)

            for nei in adjList[node]:
                # a loop detected means we don't have a valid order
                if dfs(nei) == False:
                    return False
            
            # for current node, no more neighbors, means it have no prerequisites. end node , so we add to res
            cycle.remove(node)
            res.append(node) # node is a string
            seen.add(node) # this node is visited. next time we see it, can return True directly
            return True
        
        for node in adjList: # iterate all the node, the traveral order wil not be influenced

            if dfs(node) == False:
                return ''
        
        res.reverse()
        return ''.join(res)