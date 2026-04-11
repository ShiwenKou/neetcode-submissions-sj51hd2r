class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # bellaman fold

        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()

            for n1, n2, cost in flights:
                if prices[n1] == float('inf'):
                    continue

                if prices[n1] + cost < temp[n2]:
                    temp[n2] = prices[n1] + cost
            prices = temp
        
        return prices[dst] if prices[dst] != float('inf') else -1