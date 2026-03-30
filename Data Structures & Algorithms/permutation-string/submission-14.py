class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        pattern = collections.Counter(s1)
        window = collections.Counter(s2[:len(s1)])
        if pattern == window:
            return True
        
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
            
            if window == pattern:
                return True
        return False