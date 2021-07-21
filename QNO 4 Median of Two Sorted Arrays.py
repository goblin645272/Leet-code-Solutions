class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        t = nums1 + nums2
        t.sort()
        ind = int(len(t) / 2)
        if len(t) % 2 != 0:
            return t[ind]
        else:
            return (t[ind] + t[ind - 1])/2
