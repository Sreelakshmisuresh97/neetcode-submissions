class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = nums1+nums2
        new_list.sort()
        l,r = 0,len(new_list)-1
        m = (l+r)//2
        if(r %2 ==0):
            return (new_list[m])
        else:
            m = (l+r)//2
            return (new_list[m]+new_list[m+1])/2    