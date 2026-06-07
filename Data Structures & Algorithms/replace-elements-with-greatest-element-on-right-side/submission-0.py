class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_list= []
        for idx in range(len(arr)-1):
            max_= max(arr[idx+1:])
            new_list.append(max_)
        new_list.append(-1)
        return new_list

        