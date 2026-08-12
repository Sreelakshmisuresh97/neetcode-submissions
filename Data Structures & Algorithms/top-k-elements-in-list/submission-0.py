class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kFreq={}
        for num in nums:
           kFreq[num]= kFreq[num]+1 if num in kFreq else 1
           
        items= sorted(kFreq.items(), key=lambda x: x[1], reverse=True)  
        first_k_elements = [tup[0] for tup in items[:k]]
        return first_k_elements
        #return list(topK)  
