class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            sortS = ''.join(sorted(s))
            if sortS not in result:
                result[sortS] = []  
            result[sortS].append(s)
        return list(result.values())