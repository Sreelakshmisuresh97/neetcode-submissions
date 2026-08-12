class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordict ={}
        #i=0
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            if sortedWord in wordict.keys():
                wordict[sortedWord].append(strs[i])
            else:
                wordict[sortedWord] = [strs[i]] 
        return list(wordict.values())        