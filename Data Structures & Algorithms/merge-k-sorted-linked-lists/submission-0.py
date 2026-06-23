# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if not any(lists):
            return None
        
        sol= None
        queue = dict()
        for i in range(len(lists)):
            queue[i]= lists[i]
        while self.check_queue_empty(queue):
            min_,queue = self.min_value(queue)
            if sol is None:
                sol= ListNode(val= min_)
                head= sol
            else:
                sol.next = ListNode(val=min_)
                sol= sol.next
            
            queue= self.clear_queue(queue)
        return head


        
        
    def clear_queue(self,queue):
        clear_list = []

        for key,value in queue.items():
            if value is not None:
                continue
            else:
                clear_list.append(key)
        for each in clear_list:
            del queue[each]
        return queue
    
    def min_value(self,queue):
        min = 10000
        min_key = None
        for key,value in queue.items():
            if value.val < min:
                min = value.val
                min_key = key
        # when you find minimum remove head from initial position
        next_= queue[min_key].next
        queue[min_key].next = None
        queue[min_key]= next_
        return min, queue
    
    def check_queue_empty(self,queue):
        if any([ll for ll in list(queue.values())]):
            return True
        else:
            False

    

            
            

        