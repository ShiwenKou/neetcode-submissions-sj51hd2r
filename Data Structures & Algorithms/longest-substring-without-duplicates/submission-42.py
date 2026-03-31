class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        res = 0
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[left])
                left += 1
            
            st.add(s[i])

            res = max(res, i - left + 1)
        return res