class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i=0
        j=0
        k=0
        while k<(m+n):
            if i==m:
                nums1[k:]= nums2[j:]
                break
            if j==n:
                nums1[k:]= nums1_copy[i:]
                break
            
            if nums1_copy[i]<=nums2[j]:
                nums1[k]=nums1_copy[i]
                i+=1
            else:
                nums1[k]= nums2[j]
                j+=1
            k+=1



