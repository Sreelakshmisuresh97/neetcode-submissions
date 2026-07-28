class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        mp = {}
        maxLength =0
        for r in range(len(s)):
            if s[r] in mp:
                l=max(mp[s[r]]+1,l)
            mp[s[r]]=r
            maxLength = max(maxLength,r-l+1)
        return maxLength     