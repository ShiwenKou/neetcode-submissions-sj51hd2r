class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        res = 0
        l = 0
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l += 1
            st.add(s[i])
            res = max(res, i - l + 1)
        return res

        