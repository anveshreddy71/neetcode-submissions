class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length= len(nums)
        i=0
        k=0
        while i<length:
            if nums[i]==val:
                k+=1
                for j in range(i,length-1):
                    nums[j]= nums[j+1]
                nums[length-1]= -1
            else:
                i+=1
        return length-k
            


                

        