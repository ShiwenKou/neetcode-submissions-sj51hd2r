class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n

        prices[src] = 0


        for _ in range(k + 1):
            copy_p = prices.copy()
            for s, d, p in flights:

                if prices[s] == float('inf'):
                    continue
                
                if prices[s] + p < copy_p[d]:
                    copy_p[d] = prices[s] + p
            
            prices = copy_p
        return -1 if prices[dst] == float('inf') else prices[dst]
