class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0


        for _ in range(k + 1):
            temp = prices.copy()
            for n1, n2, p in flights:
                if prices[n1] == float('inf'):
                    continue
                
                if prices[n1] + p < temp[n2]:
                    temp[n2] = prices[n1] + p
            prices = temp

        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]