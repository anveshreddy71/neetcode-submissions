class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        split rows by binary and then split each row
        '''
        if len(matrix)==1:
            arr = matrix[0]
            return self.search(arr, target)

        else:
            first_values= [x[0] for x in matrix]
            l= 0
            r = len(first_values)-1
            m = (l+r)//2
            if l>r:
                return False
            if first_values[m]>target:
                return self.searchMatrix(matrix[:m],target)
            elif first_values[m]<target:
                if self.search(matrix[m],target):
                    return True
                return self.searchMatrix(matrix[m+1:],target)
            else:
                return True
    
    def search(self, nums: List[int], target: int) -> int:
        l= 0
        r = len(nums)-1
        if l>r:
            return False
        m = (l+r)//2
        if nums[m]>target:
            return self.search(nums[:m],target)
        elif nums[m]<target:
            return self.search(nums[m+1:],target)
        else:
            return True
        return False



        