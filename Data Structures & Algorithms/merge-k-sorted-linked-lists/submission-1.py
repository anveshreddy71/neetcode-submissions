# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        1. divide and conquer rule
        2. split lists and merge two at a time recursively
        '''
        if not lists:
            return None
        if not any(lists):
            return None
        if len(lists)==1:
            return lists[0]
        elif len(lists)==2:
            return self.mergetwolists(lists[0],lists[1])
        else:
            new= self.mergetwolists(lists[0],lists[1])
            new_list= [new]+ lists[2:]
            return self.mergeKLists(new_list)
    
    def mergetwolists(self, list1, list2):
        '''
        merge two lists with three pointer, two at current positions(heads) of
        list 1,2 and other at new list current position
        '''
        p1= list1
        p2= list2
        ll=None
        while p1 and p2:
            if p1.val<=p2.val:
                if not ll:
                    ll= p1
                    head= ll
                else:
                    ll.next = p1
                    ll = ll.next
                p1= p1.next
            else:
                if not ll:
                    ll= p2
                    head= ll
                else:
                    ll.next = p2
                    ll = ll.next
                p2= p2.next
            
            if not p1:
                ll.next = p2
            if not p2:
                ll.next = p1
        
        return head



    
