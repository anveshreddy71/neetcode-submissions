class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l= 0
        r = len(nums)-1
        if l>r:
            return -1
        m = (l+r)//2
        if nums[m]>target:
            return self.search(nums[:m],target)
        elif nums[m]<target:
            res= self.search(nums[m+1:],target)
            return m+res+1 if res!=-1 else -1
        else:
            return m
        return -1
        