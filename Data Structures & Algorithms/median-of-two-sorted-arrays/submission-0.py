class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tlist = sorted(nums1+nums2)
        print(tlist)
        if len(tlist)%2 == 0:
            tlen = int((len(tlist))/2)
            return (tlist[tlen-1]+tlist[tlen])/2
        else:
            tlen = int((len(tlist)-1)/2)
            return tlist[tlen]