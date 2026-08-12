class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l = 0
        max_f=  0
        for r in range(len(s)):
            charCount[s[r]]=1+charCount.get(s[r],0)
            max_f = max(max_f,charCount[s[r]])

            if (r-l+1)-max_f>k:
                charCount[s[l]]-=1
                l+=1
        return r-l+1        